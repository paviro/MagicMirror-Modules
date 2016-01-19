#!/usr/bin/python
# coding: utf8
"""PaViRO MagicMirror-Extensions - Face recognition
Face Recognition Testing Script
Copyright 2015 Paul-Vincent Roll
Based on work by Tony DiCola (Copyright 2013)
"""
import socket
import os, os.path
import time
import face
import cv2
import config
import syslog
import socket
from thread import start_new_thread

syslog.syslog("Facerecognition started...")

current_user = None
last_match = None
bewegung = "true"
angemeldet = 0
gleicher_nutzer_in_folge = 0

def node_bridge(send_command, socket_file):
	if os.path.exists( socket_file ):
		client = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
		client.connect( socket_file )
		client.send( send_command )
		client.close()
	else:
		syslog.syslog("Couldn't Connect!")

#This is listening for another script and waits for motion detected by a motion sensor. Does nothing in this release.
def socket_server(nothing):
	global bewegung
	sockfile = "/tmp/facerec.sock"

	if os.path.exists( sockfile ):
		os.remove( sockfile )
	syslog.syslog("Opening socket...")

	server = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
	server.bind(sockfile)
	server.listen(5)
	syslog.syslog("Listening...")
	while True:
		time.sleep(0.2)
		conn, addr = server.accept()

		while True: 

			data = conn.recv( 1024 )
			if not data:
					break
			else:
					bewegung = data
					syslog.syslog("-" * 20)
					syslog.syslog("Bewegungsdaten erhalten...")
					syslog.syslog("Bewegung: " + bewegung)
					syslog.syslog("-" * 20)
	syslog.syslog("-" * 20)
	syslog.syslog("Shutting down...")

	server.close()
	os.remove( sockfile )
	
start_new_thread(socket_server, (None,))	

# Load training data into model
syslog.syslog('Loading training data...')
print config.POSITIVE_THRESHOLD
if config.RECOGNITION_ALGORITHM == 1:
	syslog.syslog("ALGORITHM: LBPH")
	model = cv2.createLBPHFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)
elif config.RECOGNITION_ALGORITHM == 2:
	syslog.syslog("ALGORITHM: Fisher")
	model = cv2.createFisherFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)
else:
	syslog.syslog("ALGORITHM: Eigen")
	model = cv2.createEigenFaceRecognizer(threshold=config.POSITIVE_THRESHOLD)

model.load(config.TRAINING_FILE)
syslog.syslog('Training data loaded!')

camera = config.get_camera()

while True:
		time.sleep(0.5)
		if bewegung == "true":
			# Get image
			image = camera.read()
			# Convert image to grayscale.
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			# Get coordinates of single face in captured image.
			result = face.detect_single(image)
			if result is None:
				if (time.time() - angemeldet > 15 and current_user != None):
					syslog.syslog("Benutzer " + current_user + " abgemeldet.")
					node_bridge("Gesicht;Abgemeldet", "/tmp/python_node_bridge")
					gleicher_nutzer_in_folge = 0
					current_user = None
				continue
			x, y, w, h = result
			# Crop and resize image face.
			if config.RECOGNITION_ALGORITHM == 1:
				crop = face.crop(image, x, y, w, h)
			else:
				crop = face.resize(face.crop(image, x, y, w, h))
			# Test face against model.
			label, confidence = model.predict(crop)
			if (label !=-1 and label!=0):
				angemeldet = time.time()
				#Routine, zum Zählen, wie oft der selbe Nutzer in Folge erkannt wurde.
				if (config.personen[label] == last_match and gleicher_nutzer_in_folge < 2):
					gleicher_nutzer_in_folge = gleicher_nutzer_in_folge + 1
				if config.personen[label] != last_match:
					gleicher_nutzer_in_folge = 0
				#Nutzer wird nur gewechselt, wenn mindestens zweimal der gleiche, neue Nutzer hintereinander erkannt wurde.	
				if (config.personen[label] != current_user and gleicher_nutzer_in_folge > 1):
					current_user = config.personen[label]
					#Momentaner benutzer wird zu nodejs geschickt.
					syslog.syslog("Benutzer " + config.personen[label] + " wurde mit Wahrscheinlichkeit " + str(confidence)  + " angemeldet.")
					node_bridge("Gesicht;" + config.personen[label], "/tmp/python_node_bridge")
				last_match = config.personen[label]
			elif (current_user != "Unbekannt" and time.time() - angemeldet > 5):
				current_user = "Unbekannt"
				node_bridge("Gesicht;" + current_user, "/tmp/python_node_bridge")
				syslog.syslog(current_user + "er Benutzer erkannt.")
			else:
				syslog.syslog('Unbekannter Benutzer')
				continue
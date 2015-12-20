'use strict';
var io = require('socket.io').listen(1234);
var net = require('net');

process.on('uncaughtException', function (err) {
  console.log("[" + Date() + "]: " + err);
  //io.sockets.emit('error', "[" + Date() + "]: " + err);
});

//Callmonitor
//Setup
require('./addressbook.js');
var CallMonitor = require('node-fritzbox-callmonitor');
var fritzbox = {
  address: '192.168.178.1', //change IP here!
  port: '1012'
};
var monitor = new CallMonitor(fritzbox.address, fritzbox.port);

//Logic
monitor.on('inbound', function (call) {
    if (call.caller != "") {
        if (obj[call.caller]) { 
            io.sockets.emit('anruf', obj[call.caller]);
        }
        if (!obj[call.caller]) { 
            io.sockets.emit('anruf', call.caller);
        }
        };
});

monitor.on('disconnected', function (call) {
    io.sockets.emit('anruf', 'clear');
});

//End Callmonitor
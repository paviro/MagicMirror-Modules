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

//Python Bridge - needed for faceregognition
var server = net.createServer(function(python_bridge) {
  python_bridge.on('data', function(data) {
    if(data.toString().split(";")[0] == "Gesicht") {
      console.log(data.toString().split(";")[1])
      io.sockets.emit('Gesicht', data.toString().split(";")[1]);
    }
    if(data.toString() == "DONE") {
      python_bridge.end();
        }
  });
});
server.listen("/tmp/python_node_bridge");
//End Python Bridge
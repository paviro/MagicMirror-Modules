# MagicMirror-Extensions
In this repository I will with time open source the [MagicMirror](https://github.com/MichMich/MagicMirror) extensions I wrote for my mirror. You can find some more details on my [blog](http://metype.org/en/category/diy-projekte/spiegel/).

## Features
- Callmonitor for FRITZ!Box users

### Future releases (implemented but not yet releasable)
- Faceregognition and personalized view for recognized faces.
- Online banking through HBCI (displaying how much money you have on your bank account)
- Multiple calenders based on faceregognition

## Usage
1. Copy the folder `www/modules/paviro` into `modules` inside your mirrors webserver.
2. Copy the folder SocketIOServer in `bin` into `/usr/local/bin` on your Pi or another mirror computer.
3. Change the IP adress in `SocketIOServer/server.js` to the IP of your FRITZ!Box.
4. Add your adressbook in `SocketIOServer/addressbook.js`.
5. Install node.js [(instructions)](http://blog.wia.io/installing-node-js-v4-0-0-on-a-raspberry-pi/)
6. Open a terminal and change into `SocketIOServer` by using `cd /usr/local/bin/SocketIOServer` then install the dependencies (see bellow).
7. Activate the callmonitor of your FRITZ!Box by calling `#96*5*` on a connected phone.
8. Run the script by executing `node server.js` in the SocketIOServer folder.
9. Add the server.js to your autostart.

## Dependencies
- [node-fritzbox-callmonitor](https://www.npmjs.com/package/node-fritzbox-callmonitor) (npm install node-fritzbox-callmonitor)
- [socket.io](http://socket.io/) (npm install socket.io)
- [OpenCV](http://opencv.org) (sudo apt-get install libopencv-dev python-opencv)

## Open Source Licenses
###[pi-facerec-box](https://github.com/tdicola/pi-facerec-box)
The MIT License (MIT)

Copyright (c) 2014 Tony DiCola

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The negative training data is from the ORL face database.  Please see the file
tools/facetrainer/training_data/negative/README for more information on this data.

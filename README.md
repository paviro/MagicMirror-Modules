# MagicMirror-Extensions
In this repository I will with time open source the [MagicMirror](https://github.com/MichMich/MagicMirror) extensions I wrote for my mirror. You can find some more details on my [blog](http://metype.org/en/category/diy-projekte/spiegel/).

## Features
- Callmonitor for FRITZ!Box users

### Future releases (implemented but not yet releasable)
- Faceregognition and personalized view for recognized faces.
- Online banking through HBCI (displaying how much money you have on your bank account)
- Multiple calenders based on faceregognition

## Usage
1. Copy the folder `callmonitor` from `www/js` into your webservers `js` folder.
2. Copy the folder `img` from `www` into your webservers root folder.
3. In your index.php add <br>`<script src="http://localhost:1234/socket.io/socket.io.js"></script>
<script src="js/callmonitor/callmonitor.js" type="text/javascript"></script>`<br> before `</body>` and remove the existing refrence to socket.io.js
4. Copy the folder SocketIOServer in `bin` into `/usr/local/bin` on your Pi or another mirror computer.
5. Change the IP adress in `SocketIOServer/server.js` to the IP of your FRITZ!Box.
6. Add your adressbook in `SocketIOServer/addressbook.js`.
7. Install node.js [(instructions)](http://blog.wia.io/installing-node-js-v4-0-0-on-a-raspberry-pi/)
8. Open a terminal and change into `SocketIOServer` by using `cd /usr/local/bin/SocketIOServer` then install the dependencies (see bellow).
9. Activate the callmonitor of your FRITZ!Box by calling `#96*5*` on a connected phone.
10. Run the script by executing `node server.js` in the SocketIOServer folder.
11. Add the server.js to your autostart.

## Dependencies
- [node-fritzbox-callmonitor](https://www.npmjs.com/package/node-fritzbox-callmonitor) (npm install node-fritzbox-callmonitor)
- [socket.io](http://socket.io/) (npm install socket.io)

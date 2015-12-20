//connect do Call monitor
//localStorage.debug = '*';

//Add callmonitor CSS 
$('body').append('<link rel="stylesheet" href="js/callmonitor/css/style.css">')

//Add call alert
$('body').append(`

<div class="center-ver center-hor">

<div id="call" class="light"><img src="img/phone.png" height="80px"><h2>Incoming call</h2><div id="caller">"number goes here"</div></div>

</div>

`);

var socket = io.connect('http://localhost:1234');
socket.on('anruf', function (data){
    if (data != 'clear'){
            $('#call').fadeIn(700);
            $('.lower-third').fadeOut(700);
            $('#caller').text(data);
    }
    if (data == 'clear'){
    $('#call').fadeOut(700);
    $('.lower-third').fadeIn(700);
    }
});
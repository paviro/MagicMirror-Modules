//connect do Call monitor
//localStorage.debug = '*';

function switchview(person) {
    if (person !="Abgemeldet" && person !="Unbekannt"){
        //Set calender URL for logged in user currently only one URL is supported.
        config.calendar.url = "https://example.com/your-calendar-url"
        calendar.updateData()
    }
    if (person == "Abgemeldet"){
        //set URL for not logged in user.
        config.calendar.url = "http://ifeiertage.de/bw-sk.ics"
        calendar.updateData()
    };
};


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

socket.on('Gesicht', function (data) {
    if (data != "Abgemeldet"){
        $('#anmeldung').fadeIn(700);
        $('.lower-third').fadeOut(700);
        $('#anmelde_name').text(data);
        $('#anmeldung').delay(5000).fadeOut(700);
        $('.lower-third').delay(5000).fadeIn(700);
    };
    switchview(data)
});

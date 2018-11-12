$(document).ready(function () { 
    $('select.turn_dates').bind('click', function (e) {
        $('select.turn_dates option').removeClass('select');
        if(e.target.tagName === 'SELECT') {
            var id = '#' + e.target.value;
            $(id).toggleClass('select');
        }
    });
    $('select.turn_dates').bind('click', function (e) {
        $('select.turn_dates option').removeClass('select');
        if(e.target.tagName === 'SELECT') {
            var id = '#' + e.target.value;
            $(id).toggleClass('select');
        }
    });
    $('#send-turn').bind('click', function(e) {
        confirm('Su cita ha sido correctamente enviada. Le esperamos en la fecha citada!!.');
        // alert('Su cita ha sido correctamente enviada. Le esperamos en la fecha citada!!.');
    });
 })
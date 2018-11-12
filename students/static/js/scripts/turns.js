$(document).ready(function () { 
    $('select.turn_dates').bind('click', function (e) {
        alert('HERE');
        $('select.turn_dates option').removeClass('select');
        if(e.target.tagName === 'SELECT') {
            var id = '#' + e.target.value;
            $(id).toggleClass('select');
        }
    });
 })
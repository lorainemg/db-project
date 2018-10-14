var refresh_icons = function (field_id) {
    var from = $('#' + field_id + '_from');
    var to = $('#' + field_id + '_to');
    // Active if at least one item is selected
    $('#' + field_id + '_add_link').toggleClass('active', any_selected(from));
    $('#' + field_id + '_remove_link').toggleClass('active', any_selected(to));
    // Active if the corresponding box isn't empty
    $('#' + field_id + '_add_all_link').toggleClass('active', from.find('option').length > 0);
    $('#' + field_id + '_remove_all_link').toggleClass('active', to.find('option').length > 0);
};

var filter_key_press = function (event, field_id) {
    var from = document.getElementById(field_id + '_from');
    // don't submit form if user pressed Enter
    if ((event.which && event.which === 13) || (event.keyCode && event.keyCode === 13)) {
        from.selectedIndex = 0;
        SelectBox.move(field_id + '_from', field_id + '_to');
        from.selectedIndex = 0;
        event.preventDefault();
        return false;
    }
};

var filter_key_up = function (event, field_id) {
    var from = document.getElementById(field_id + '_from');
    var temp = from.selectedIndex;
    SelectBox.filter(field_id + '_from', document.getElementById(field_id + '_input').value);
    from.selectedIndex = temp;
    return true;
};

var filter_key_down = function (event, field_id) {
    var from = document.getElementById(field_id + '_from');
    // right arrow -- move across
    if ((event.which && event.which === 39) || (event.keyCode && event.keyCode === 39)) {
        var old_index = from.selectedIndex;
        SelectBox.move(field_id + '_from', field_id + '_to');
        from.selectedIndex = (old_index === from.length) ? from.length - 1 : old_index;
        return false;
    }
    // down arrow -- wrap around
    if ((event.which && event.which === 40) || (event.keyCode && event.keyCode === 40)) {
        from.selectedIndex = (from.length === from.selectedIndex + 1) ? 0 : from.selectedIndex + 1;
    }
    // up arrow -- wrap around
    if ((event.which && event.which === 38) || (event.keyCode && event.keyCode === 38)) {
        from.selectedIndex = (from.selectedIndex === 0) ? from.length - 1 : from.selectedIndex - 1;
    }
    return true;
};

var any_selected = function (field) {
    var any_selected = false;
    try {
        // Temporarily add the required attribute and check validity.
        // This is much faster in WebKit browsers than the fallback.
        field.attr('required', 'required');
        any_selected = field.is(':valid');
        field.removeAttr('required');
    } catch (e) {
        // Browsers that don't support :valid (IE < 10)
        any_selected = field.find('option:selected').length > 0;
    }
    return any_selected;
};

$(document).ready(function () {
    var field_id = 'id_careers';

    var move_selection = function (e, elem, move_func, from, to) {
        if (elem.className.indexOf('active') !== -1) {
            move_func(from, to);
            refresh_icons(field_id);
        }
        e.preventDefault();
    };

    $('a.selector-add').bind('click', function (e) {
        move_selection(e, this, SelectBox.move, field_id + '_from', field_id + '_to');
    });
    $('a.selector-remove').bind('click', function (e) {
        move_selection(e, this, SelectBox.move, field_id + '_to', field_id + '_from');
    });
    $('a.selector-clearall').bind('click', function (e) {
        move_selection(e, this, SelectBox.move_all, field_id + '_to', field_id + '_from');
    });
    $('#id_careers_input').bind('keypress', function (e) {
        filter_key_press(e, field_id);
    });
    $('#id_careers_input').bind('keyup', function (e) {
        filter_key_up(e, field_id);
    });
    $('#id_careers_input').bind('keydown', function (e) {
        filter_key_down(e, field_id);
    });
    $('div.selector').bind('change', function (e) {
        if (e.target.tagName === 'SELECT') {
            refresh_icons(field_id);
        }
    });
    $('div.selector').bind('dblclick', function (e) {
        if (e.target.tagName === 'OPTION') {
            if (e.target.closest('select').id === field_id + '_to') {
                SelectBox.move(field_id + '_to', field_id + '_from');
            } else {
                SelectBox.move(field_id + '_from', field_id + '_to');
            }
            refresh_icons(field_id);
        }
    });
    SelectBox.init(field_id + '_from');
    SelectBox.init(field_id + '_to');
    // Move selected from_box options to to_box
    SelectBox.move(field_id + '_from', field_id + '_to');
});
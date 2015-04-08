function clear_page() {
    $('section').empty();
    $('body').addClass('loading');
    $('body').removeClass('up');
    var spinner = $('#spinner').html();
    $('section').append(spinner);
    console.log('Cleared Page');
}

function load_database() {
    clear_page();
    $.ajax({
        type: 'POST',
        url: '/',
        dataType: "json",
        success: function(entries) {
            console.log('Retrieved Database');
            window.entries = entries;
            render_page();
        }
    });
}

function render_page() {
    window.entries = entries;
    $(entries).each(function(index, value) {
          var title = value[Object.keys(value)[2]];
          var description = value[Object.keys(value)[3]];
          var category = value[Object.keys(value)[0]];
          var template = $('#entry').html().format(title, description, category);
          $('section').append(template);
    });
    $('.spinner').remove();
    $('body').removeClass('loading');
    console.log('Rendered Page');
}

function add_entry(entry) {
    clear_page();
    $.ajax({
        url: '/',
        type: 'post',
        dataType: "json",
        data: entry.jsonObject(),
        success: function(entries) {
            console.log("Retrieved Database");
            window.entries = entries;
            render_page();
            }
    });
    console.log("Sent New Entry");
}

function update_local_entry(entry) {
    var title = entry[0][0]['value'];
    var description = entry[0][1]['value'];
    var category = entry[0][2]['value'];
    var template = $('#entry').html().format(title, description, category);
    if ( $('#live_template' ).length ) {
        $('div[id=live_template]').remove();
        $('section').append(template);
        $('section div:last-child').attr('id','live_template');
    } else {
        $('section').append(template).focus();
        $('section div:last-child').attr('id','live_template');
    }
}

$.fn.jsonObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return JSON.stringify(o);
};

String.prototype.format = function() {
  var args = arguments;
  return this.replace(/{(\d+)}/g, function(match, number) {
        return typeof args[number] != 'undefined'
          ? args[number]
          : match
        ;
  });
};

$( document ).ready(function() {
    load_database();

    $('input[value="Add Entry"]').click(function() {
        add_entry($('#entryform'));
        $('#entryform *').empty();
    });

    $('#entryform').keyup(function() {
        update_local_entry($('#entryform'));
        $('html, body').animate({
           scrollTop: $(document).height()-$(window).height()},
           1000,
           "swing"
        );
    });

    $('nav div').click(function() {
        if ($('body').hasClass('up') ) {
            $('body').removeClass('up');
        } else {
            $('body').addClass('up');
        }
    });
});

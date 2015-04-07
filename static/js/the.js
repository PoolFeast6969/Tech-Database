function clear_page() {
    $('section').empty();
    $('body').addClass('loading');
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
        success: function(data) {
            console.log('Retrieved Database');
            window.data = data;
            render_page();
        }
    });
}

function render_page() {
    window.data = data;
    $(data).each(function(index, value) {
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

function send(outgoing) {
    clear_page();
    $.ajax({
        url: '/',
        type: 'post',
        dataType: "json",
        data: outgoing.jsonObject(),
        success: function(data) {
            console.log("Retrieved Database");
            window.data = data;
            render_page();
            }
    });
    console.log("Sent New Entry");
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
});

function submit_form() {
    send($('#addentry'));
}

function clear_page() {
    $('section').empty();
    $('body').addClass('loading');
    var spinner = $('#spinner').html();
    $('section').append(spinner);
    load_database();
}

function load_database() {
    $.ajax({
        type: 'POST',
        url: '/',
        dataType: "json",
        success: function(data) {
          console.log('Retrieved Database');
          render_page(data);
        }
    });
}

function render_page(data) {
    $(data).each(function(index, value) {
      var title = value[Object.keys(value)[2]];
      var description = value[Object.keys(value)[3]];
      var category = value[Object.keys(value)[0]];
      var template = $('#entry').html().format(title, description, category);
      $('section').append(template);
    });
    $('.spinner').remove();
    $('body').removeClass('loading');
}

function send_to_database(e) {
    $.ajax({
        type: 'POST',
        url: '/',
        data: $(this).serialize(),
        success: function() { load_database(); }
    });
    e.preventDefault();
}

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
    clear_page();
});

function load_database() {
    $('body').addClass('loading');
    $.ajax({
        type: 'POST',
        url: '/',
        dataType: "json",
        success: function(data) {
          console.log('Retrieved Database');
          $('body').removeClass('loading');
          window.data = data;
        }
    });
}

function render_database() {
    window.data = data;
    $(data).each(function(index, value) {
      var title = value[Object.keys(value)[2]];
      var description = value[Object.keys(value)[3]];
      var category = value[Object.keys(value)[0]];
      console.log(title + " " + category + " " + description);
    });
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

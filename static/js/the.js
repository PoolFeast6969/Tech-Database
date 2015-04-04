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
      console.error(value);
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

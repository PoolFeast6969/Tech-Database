function render_database() {
    somehow
}

function load_database() {
    $.ajax({
        type: 'POST',
        url: '/',
        success: function(data) {console.log(data);}
    });
}

$('form').submit(function(e) {
    $.ajax({
        type: 'POST',
        url: '/',
        data: $(this).serialize(),
        success: function() {load_database();}
        }
    });
    e.preventDefault();
});

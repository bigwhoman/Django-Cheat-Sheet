$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'search',
        data: {
            word: $('#word').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('h2').html(data)
        }
    });
});
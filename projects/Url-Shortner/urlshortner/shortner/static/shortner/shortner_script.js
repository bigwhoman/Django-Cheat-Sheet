$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: 'shortner/create',
        data: {
            link: $('#link').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            $('h2').html("localhost/8000" + data)
        }
    });
});
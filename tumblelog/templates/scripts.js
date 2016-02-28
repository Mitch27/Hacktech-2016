$(document).ready(function(e) {
    $("form").submit(function(e) {
        e.preventDefault();

        var form_data = $(this).serialize();
        var form_url = $(this).attr("action");
        var form_method = $(this).attr("method").toUpperCase();

        $.ajax({
            url: form_url,
            type: form_method,
            data: form_data,
            cache: false
            // success: success cb here...
        });
    });
});

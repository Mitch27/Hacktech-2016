$(document).ready(function() {
  $('form').submit(function(e) {
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function () {
        console.log("Success!");
      }
    });
    e.unbind();
  });
});

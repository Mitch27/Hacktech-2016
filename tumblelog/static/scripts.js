$(document).ready(function() {
    $("#add-profile-btn").click(function() {
        $("#add-profile-btn").hide();
        $("#add-profile-form").show();
    });
    $("#close-profile-btn").click(function() {
        $("#add-profile-btn").show();
        $("#add-profile-form").hide();
    });
});

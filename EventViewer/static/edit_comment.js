$(document).ready(function () {
    // Hide all edit forms initially
    $('form[id^="edit_comment_"]').hide();
    // Show the edit form when the Edit link is clicked
    $('a[href^="#edit_comment_"]').click(function () {
        var form_id = $(this).attr('href');
        $(form_id).show();
        $(form_id + ' textarea').focus();
    });
    // Hide the edit form when the Save button is clicked
    $('form[id^="edit_comment_"] button[type="submit"]').click(function () {
        $(this).parents('form').hide();
    });
});
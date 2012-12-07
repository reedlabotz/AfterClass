function addMessage(text, extra_tags) {
    var message = $('<div class="'+extra_tags+'">'+text+'</div>').hide();
    $("#messages").append(message);
    message.fadeIn(500);

    setTimeout(function() {
        message.fadeOut(500, function() {
            message.remove();
        });
    }, 3000);
}
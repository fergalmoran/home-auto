$('#outputstring').hide();
$(function () {
    $(".dropdown-menu a").click(function () {
        $(".btn:first-child").text($(this).text());
        $(".btn:first-child").val($(this).text());
    });
});

$('#action-button').click(function (e) {
    var direction = $('#action-button').text() === 'Encode' ? 1 : 0;
    e.preventDefault();
    var data = JSON.stringify({
        inputstring: $('#inputstring').val(),
        direction: direction
    });
    console.log(data);
    $.ajax({
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        url: '/api/base64',
        data: data,
        success: function (r) {
            $('#outputstring').show();
            $('#outputstring').val(r.outputstring);
        },
        dataType: 'json'
    });
});
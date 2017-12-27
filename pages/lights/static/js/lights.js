$(document).ready(function () {
    let selectedLight = $('#camera');
    let selectedBrightness = $('#brightness').slider({
        formatter: function (value) {
            return 'Current value: ' + value;
        }
    });
    $('#controls').hide();

    selectedLight.empty();

    selectedLight.append('<option selected="true" disabled>Choose Light</option>');
    selectedLight.prop('selectedIndex', 0);

    $.getJSON('/api/camera', function (data) {
        let options = '';
        $.each(data, function (key, value) {
            options += '<option value=' + key + '>' + value + '</option>';
        });
        selectedLight.empty();
        selectedLight.append(options);
        selectedLight.selectpicker('refresh');

        $('#controls').show();

    });

    $('form').submit(function (e) {
        e.preventDefault();

        let light = $('#camera').find(":selected").text();
        let brightness = selectedBrightness.slider('getValue');
        let colour = $('#colourpicker').val().replace('#', '');
        let data =
            `{
                "mode": {
                    "${light}": {
                        "on": true,
                        "brightness": ${brightness},
                        "rgb": "${colour}"
                    }
                }
            }`;
        console.log(JSON.parse(data));
        $.ajax({
            type: 'POST',
            contentType: "application/json; charset=utf-8",
            url: '/api/camera/recipe/execute',
            data: data,
            success: function (r) {
            },
            dataType: 'json'
        });
        return false;
    });
});

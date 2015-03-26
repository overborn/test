$(function () {
    $('#car').change(function(){
        var car = $(this).val();
        $.get('/suggest_models/', {car: car}, function(data){
            var models = data.models;
            $('#model').empty()
            for (var i = 0; i < models.length; i++) {
                $('#model').append($('<option>', {
                    value: models[i],
                    text: models[i]
                }));                
            };
        })
    })
    $('#car').change();
});
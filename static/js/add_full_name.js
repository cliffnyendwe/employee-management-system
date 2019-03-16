$(function () {
    var firstName = '', lastName = '';
    $('input[name=first_name]').on('keyup keypress blur change', function () {
        firstName = $(this).val();
        updateFullName()
    });
    // $('input[name=last_name]').on('keyup keypress blur change', function () {
    //     lastName = $(this).val();
    //     updateFullName()
    // });
    function updateFullName() {
        if ($('input[name=first_name]').val() === '' && $('input[name=last_name]').val() === '') {
            $('input[name=full_name]').val('');
        } else {
            $('input[name=full_name]').val(firstName + ' ' + lastName);
        }
    }

});



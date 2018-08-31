$(document).ready(function($){
    chkboxValidate();
    $('.taskilon-status--input').click(function(){
        chkboxValidate();
    });
    if( $('#id_email').length > 0 ) float();

    function float(){
        var email = $('#id_email');
        checkVal(email);
        email.on('change keyup', function(){
            checkVal(email);
        });
    }
    function checkVal(email) {
		( email.val() == '' ) ? email.parent('div').removeClass('floating-label') : email.parent('div').addClass('floating-label');
	}

    function chkboxValidate(){
        var checkboxInput = $('.taskilon-status--input');
        if($(checkboxInput).prop("checked") == true){
            $(checkboxInput).next().attr('title', 'Active');
        }
        else if($(checkboxInput).prop("checked") == false){
            $(checkboxInput).next().attr('title', 'Completed');
        }
    }

});

$(document).ready(function($){
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

});

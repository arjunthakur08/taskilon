$(document).ready(function(){

    menuWideOrMobile();
    $(window).resize(function(){
        menuWideOrMobile();
    });

    $('#nav-trigger-link').click(function(){
       if($('#nav-trigger-link').hasClass('expanded')){
           $('#nav-trigger-link.expanded').removeClass('expanded');
           $('#nav.nav-open').removeClass('nav-open');
       }
       else{
           $('#nav-trigger-link').addClass('expanded');
           $('#nav').addClass('nav-open');
       }
    });
});

$(window).on('load', function(){
    // Messages Self-Destruction
    (function(){
        setTimeout(function(){
            $('.success').fadeOut(1000, function(){
                $('.success').remove();
            });
        }, 5000);
    })();
    if($('.message').hasClass('error'))
    {
        $('#myModal').css('display','block');
    }
});

function menuWideOrMobile(event){
	// Mobile
	if($(window).width()<768)
	{
		$("#nav").addClass("on-mobile");
		$("#wide").addClass("mobile");
        $('#trigger').addClass('mobile');
	}

	//Not Mobile
	else
	{
		$("#nav").removeClass("on-mobile");
		$("#wide").removeClass("mobile");
        $('#trigger').removeClass('mobile');
	}
}

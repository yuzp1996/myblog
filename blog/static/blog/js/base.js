$(function(){
$("#qrcode").click(function()
	{
		address = $("#myqrcode").val();
		$("#frameId").css("z-index",2);
		$("#frameId").attr("src","http://127.0.0.1:8000/qrcode/"+address+"");
    })
$(function(){  
    var $backToTopEle = $('.toTop'), $backToTopFun = function() {  
        var st = $(document).scrollTop(), winh = $(window).height();  
        (st > 200) ? $backToTopEle.fadeIn('slow') : $backToTopEle.fadeOut('slow');  
        //IE6下的定位  
        if (!window.XMLHttpRequest) {  	
            $backToTopEle.css("top", st + winh - 166);  
        }  
    };  
    $('.toTop').click(function() {  
        $("html, body").animate({ scrollTop: 0 }, 1200);  
    })  
    $backToTopEle.hide();  
    $backToTopFun();  
    $(window).bind("scroll", $backToTopFun);  
    $('#catalogWord').click(function(){  
        $("#catalog").slideToggle(600);  
    })  
})  

// $("#shape1").click(
// 	$(document.body).animate({'scrollTop':0},1000);
// 	)


})		

$('#load').click(function() {  
    $("html, body").animate({ scrollTop: 800}, 1200);  
})  
$('#load1').click(function() {  
    $("html, body").animate({ scrollTop: 1600}, 1200);  
})  
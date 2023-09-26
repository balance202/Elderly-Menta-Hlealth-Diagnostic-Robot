/****************************************************************
 *																*		
 * 						      代码库							*
 *                        www.dmaku.com							*
 *       		  努力创建完善、持续更新插件以及模板			*
 * 																*
****************************************************************/

jQuery(document).ready(function($){
    jQuery('.faq_block .panel-heading').eq(0).addClass('active');
    jQuery('.faq_block .panel-heading').click(function(){
        if(jQuery(this).hasClass('active')){
            jQuery(this).removeClass('active');
        }
        else{
            jQuery('.faq_block .panel-heading').removeClass('active');
            jQuery(this).toggleClass('active');
        }
    });



    jQuery("#slide-about").owlCarousel({

      navigation : true,
      slideSpeed : 300,
      paginationSpeed : 400,
      singleItem : true

      // "singleItem:true" is a shortcut for:
      // items : 1, 
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

    });



    jQuery('#zo2-top-wrap .icon-search').click(function(){
        jQuery('.search .search-form').fadeIn('300');
        jQuery('#zo2-top-wrap .search .search-form .inputbox').focus().css("color","#000");
    });
        jQuery('#zo2-top-wrap .search-close').click(function(){
        jQuery('.search .search-form').fadeOut('300');
    });


     jQuery('#images').imagesLoaded(function() {
        jQuery(this).masonry({
            itemSelector: '.pic',
            columnWidth: 15,
            isAnimated: true,
            layoutPriorities: {
                shelfOrder: 1.1
            }
        });
    });



    var owl = jQuery("#zt-logo-brand .custom");
    owl.owlCarousel({
        autoPlay: 3000,
        items : 6,
        navigation : true,
        pagination : false,
        slideSpeed : 500
    });


    var randomScalingFactor = function(){ return Math.round(Math.random()*100)};
    var lineChartData = {
        labels : ["11:05", "12:05","13:05","14:05","15:05"],
        datasets : [
            {
               
               fillColor : "#b2eaff",
                strokeColor : "rgba(255,255,255,1)",
                pointColor : "#21c2f8",
                pointStrokeColor : "#fff",
                pointHighlightFill : "#fff",
                pointHighlightStroke : "rgba(220,220,220,1)",
                data : [28,68,40,19,96]
            }
        ]

    }

    window.onload = function(){
        if( document.getElementById("line")!= null){
        var ctx = document.getElementById("line").getContext("2d");
        window.myLine = new Chart(ctx).Line(lineChartData, {
            responsive: false
        });
    }
    }




    var IGPbRevealObjects  = null;
    var IGPbStellarObjects = null;
    $(document).ready(function (){
        // Enable Appearing animations for elements
        if($('[data-scroll-reveal]').length) {
            if (!IGPbRevealObjects) {
                IGPbRevealObjects = new scrollReveal({
                        reset: true
                    });
            }
        }
        // Enable paralax for row container
        if($('[data-stellar-background-ratio]').length) {
            if (!IGPbStellarObjects) {
                IGPbStellarObjects = $.stellar({
                    horizontalScrolling: false,
                    verticalOffset: 40
                });
            }
        }
    });


}(jQuery));


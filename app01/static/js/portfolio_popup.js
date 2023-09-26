/*!

	Surmoi - Resume, CV, vCard, Portfolio Template
	Copyright (c) 2015, Subramanian 

	Author: Subramanian
	Profile: themeforest.net/user/FMedia/
	
	Version: 1.0.0
	Release Date: April 2015
	
*/	


"use strict";

		  
		  
$(document).ready(function(){
	
	// Flex slideshow initialize
	$("body").find('.flexSlideshow').each(function(){
			try{
			
				var aniTyp = $(this).hasClass('slideAnimation') ? "slide" : "fade";
				var tim_ = $(this).attr('data-slidetime') ?  Math.abs($(this).attr('data-slidetime')) : 5000;
				
											
				if(aniTyp === "slide"){
					$(this).find("li").each(function(i){
						$(this).find("img").show();
					});
				}

				$(this).addClass("flexslider");		
				var ffx = $(this);
				ffx.removeClass('flexSlideshow');

				var flexs = $(this);
				
				flexs.flexslider({
				slideshow: true,
				animation: aniTyp,
				slideshowSpeed: tim_,
				start: function(slider){
					flexs.data("slid",slider);
					flexs.find(".slider_loading").remove();
					slider.pause();
					}
				});	
					
			} catch (e) { }				
		});
		
	
	try {  $(".container").fitVids(); } catch (e) { }
	try {  $(".container-fluid").fitVids(); } catch (e) { }	
	
				
});		


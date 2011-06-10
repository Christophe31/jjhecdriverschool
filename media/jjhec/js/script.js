$(document).ready(function(){
  $("a.new_window").attr("target", "_blank");
  	$(function(){
		$("#faded").faded({
			speed: 500,
			crossfade: true,
			autoplay: 10000,
			autopagination:false
		});
		
		$('#domain-form').jqTransform({imgPath:'jqtransformplugin/img/'});
	});
	new ElementMaxHeight();
 });
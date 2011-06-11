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
    Cufon.now();
 });

function loginFormKeyPressed(field, evt){
  var keycode;
  if (window.event)
    keycode = window.event.keyCode;
  else if (evt)
    keycode = evt.which;
  else
    return true;
  if (keycode == 13){
    field.form.submit();
    return false;
  }
  else
    return true;
}

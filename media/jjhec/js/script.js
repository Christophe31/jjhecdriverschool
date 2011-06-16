$(function(){
    $("a.new_window").attr("target", "_blank");
    var e = $("#faded");
    if (e.length != 0){
        e.faded({
            speed: 500,
            crossfade: true,
            autoplay: 10000,
            autopagination:false
        });
     }   

    if ((e = $('#domain-form')).length != 0){
        e.jqTransform({imgPath:'jqtransformplugin/img/'});
    }
    if ((e = $('.dateinput')).length != 0){
        e.datepicker();
    }
    if ((e = $('.datetimeinput')).length != 0){
        e.datetimepicker();
    }
   if ((e = $('#mycarousel')).length != 0){    
        $('#mycarousel').jcarousel({
            scroll: '2',
            animation: 'slow'
        });  
    }
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

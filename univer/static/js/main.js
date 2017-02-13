$(document).ready(function(){
  PositionCenter($("#popup"));

  $("#pc").click(function(){

  });

  $("#signin").click(function(){
    PositionCenter($("#popup"));
    $("#hidelayout, #popup").fadeIn(300);
  });

  $("#hidelayout").click(function(){
    $("#hidelayout, #popup").fadeOut(300);
  });

  $("#id_avatar").change(function(){
    $("#avatar_loader").fadeIn(300);
    readURL(this);
  });

  function PositionCenter(elem){
    elem.css({
      left: ($(window).width()-elem.outerWidth())/2 +'px',
      top:($(window).height()-elem.outerHeight())/2-30 +'px'
    })
  };

  function readURL(input) {
    if(input.files && input.files[0]){
      var reader = new FileReader();
      reader.onload = function(e){
        $("#avatar_loader").attr('src', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    }
  };

})

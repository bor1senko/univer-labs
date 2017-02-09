$(document).ready(function(){
  PositionCenter($("#popup"));
  
  $("#signin").click(function(){
    PositionCenter($("#popup"));
    $("#hidelayout, #popup").fadeIn(300);
  });

  $("#hidelayout").click(function(){
    $("#hidelayout, #popup").fadeOut(300);
  });

  function PositionCenter(elem){
    elem.css({
      left: ($(window).width()-elem.outerWidth())/2 +'px',
      top:($(window).height()-elem.outerHeight())/2-30 +'px'
    })
  };

})

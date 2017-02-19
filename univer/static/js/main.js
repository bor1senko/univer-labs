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

  $('#menu-opener').click(function (){
    if($('#menu').hasClass('mopen')){
      //close
      $('#menu').animate({right: '-250px'});
      $('#wrapperr').animate({left: '0px'});
      $('#menu').removeClass('mopen');
      $('#menu-opener').removeClass('glyphicon-remove').addClass('glyphicon-align-justify');
      $('#menu-opener').css({
        transform:''
      });
    } else {
      //open
      $('#menu').animate({right: '0px'});
      $('#wrapperr').animate({left: '-250px'});
      $('#menu').addClass('mopen');
      $('#menu-opener').removeClass('glyphicon-align-justify').addClass('glyphicon-remove');
      $('#menu-opener').css({
        transform:'translateX(65px)'
      });
    }
  });

  $('.info_user').click(function(){
    if( $('.info_menu').hasClass('info_menu_open')){
      //close
        $('.info_menu').removeClass('info_menu_open');
        $('.info_menu').css({
          height:'0'
        });
        $('#info-p3 span').css({
          transform: ''
        });
    }
     else {
      //open
        $('.info_menu').addClass('info_menu_open');
        $('.info_menu').css({
          height:'50px'
        });
        $('#info-p3 span').css({
          transform: 'rotateZ(180deg)'
        });
    }
  });

$('.dashboard-user li:first-child').click(function(){
  if ( $(this).parent('ul').hasClass('d-menu-open') ) {
    //close
      $(this).parent('ul').removeClass('d-menu-open');
      $(this).parent('ul').css({
        height:'35px'
      });
      $(this).find('.d-menu-arrow').css({
        transform: ''
      });
  }
  else {
    //open
      $(this).parent('ul').addClass('d-menu-open');
      $(this).parent('ul').css({
        height: ($(this).parent('ul').children().length-1) *21 + 35 +'px'
      });
      $(this).find('.d-menu-arrow').css({
        transform: 'rotateX(180deg)'
      });
  }
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

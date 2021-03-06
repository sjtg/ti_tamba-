(function($){
  $(function(){
    $('.dropdown-trigger').dropdown();
    $('.select').formSelect();
    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space



$(document).ready(function(){
  // MODAL
  $('.sidenav').sidenav();
	$('.fixed-action-btn').floatingActionButton();
	$('.tooltipped').tooltip();
});

var header = $('header');
var range = 200;

$(window).on('scroll', function () {

  var scrollTop = $(this).scrollTop(),
      height = header.outerHeight(),
      offset = height / 1.1,
      calc = 1 - (scrollTop - offset + range) / range;

  header.css({ 'opacity': calc });

  if (calc > '1') {
    header.css({ 'opacity': 1 });
  } else if ( calc < '0' ) {
    header.css({ 'opacity': 0 });
  }

});

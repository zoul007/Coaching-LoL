{% load template %}

window.addEventListener('load', function(){
	new Glider(document.querySelector('.carrusel__lista'), {
		slidesToShow: 1,
  		slidesToScroll: 1,
  		dots: '.carrusel__indicadores',
		arrows: {
			prev: '.carrusel__anterior',
			next: '.carrusel__siguiente'
		},
		responsive: [
			{
			  // screens greater than >= 775px
			  breakpoint: 450,
			  settings: {
				// Set to `auto` and provide item width to adjust to viewport
				slidesToShow: 2,
				slidesToScroll: 1
			  }
			},{
			  // screens greater than >= 1024px
			  breakpoint: 800,
			  settings: {
				slidesToShow: 4,
				slidesToScroll: 1
			  }
			}
		]
	});
});


// INICIO VALIDACION FORMULARIO
$(document).ready(function(){
	$("#logo" ).click(function() {
	  window.location.href = "{% url 'home' %}";
	});



});

// FIN VALIDACION FORMULARIO

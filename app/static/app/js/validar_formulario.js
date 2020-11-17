
$(document).ready(function(){

//CLIC LOGO
$("#logo" ).click(function() {
	  window.location.href = "/";
	});

// VALIDACION FORMULARIO


	//VALIDA QUE SOLO SE PUEDAN PULSAR LETRAS
	$('#nom_dis').keypress(function (e) {
	    var regex = new RegExp("^[a-zA-Z]+$");
	    var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
	    if (regex.test(str)) {
	        return true;
	    }

	    e.preventDefault();
	    return false;
});

	$(function() {

	  $("form[name='form_lol']").validate({
	    // Especifica las reglas de validacion.
	    rules: {
	    	nom_dis:{

	    		required: true,
	    		minlength: 3
	    	},
	    	nom_invocador:{
	    		required: true,
	    		minlength: 3

	    	},
	    	email_invocador: {
	    		required: true,
	        	email: true
	      	},
	      	list_servers:{
	      		required: true
	      	},
	      	list_ligas:{
	      		required: true

	      	}

	    },
	    // Especifica los mensajes de error de las reglas de validacion
	    messages: {
	    	nom_dis:{
	    		required: " Ingresa tu Nombre",
	    		minlength: "Ingresa almenos 3 letras"
	    	},
	    	nom_invocador:{
	    		required: " Ingresa tu Nombre de Invocador",
	    		minlength: "Ingresa almenos 3 Caracteres"
	    	},
	    	email_invocador: {
	    		required: " Ingresa tu Correo",
	        	email: "Favor ingresa un correo válido"
	      	},
	      	list_servers:{
	      		required: " Selecciona un Servidor"

	      	},
	      	list_ligas:{
	      		required: " Seleeciona tu Liga"
	      	}
	    },
	    submitHandler: function(form) {
	    	alert("Datos Ingresados Correctamente!!"); // MENSAJE DE EXITO AL INGRESAR LOS DATOS.
	      	form.submit();
	      	window.location.href = "/"; // ENVÍA A LA PAGINA PRINCIPAL.
	    }


	  });
	});



});

// FIN VALIDACION FORMULARIO

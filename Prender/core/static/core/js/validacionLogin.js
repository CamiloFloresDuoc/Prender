// funciones aux

function mensajeError(caja, mensaje) {
    $("#"+ caja).html(mensaje)
    $("#"+ caja).fadeIn()
};

function noError(caja){
    $("#" + caja).fadeOut()
};

// validaciones por campo

function validaNombre(){
    if ($("#usuario").val().trim().length == 0) {
        mensajeError("eUsuario","Debes ingresar tu nombre")
        return false
    } else {
        noError("eUsuario")
        return true
    }
};

function validaContrasenna(largo){
    if ($("#password").val().trim().length == 0){
        mensajeError("eContrasenna","No has ingresado tu contraseña")
        return false
    }else if ($("#password").val().trim().length < largo){
        mensajeError("eContrasenna","La Contraseña debe tener al menos "+ largo + " caracteres de largo")
        return false
    }else {
        noError("eContrasenna")
        return true
    }
};




$(document).ready(function(){
    //mensajes error ocultos hasta ser invocados
    $(".invalid-feedback").hide();

    //cuando valida nombre?
    $("#usuario").blur(function(){
        exito = validaNombre()
    });
    $("#password").blur(function(){
        exito = validaContrasenna(9)
    });

    $("#contactForm").submit(function(){
        exito = false

        if (
            !validaNombre(),
            !validaContrasenna()
        ) {
            e.preventDefault()
        }
    });
});
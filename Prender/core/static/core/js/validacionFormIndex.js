// funciones aux

function mensajeError(caja, mensaje) {
    $("#"+ caja).html(mensaje)
    $("#"+ caja).fadeIn()
};

function noError(caja){
    $("#" + caja).fadeOut()
};

function esEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

//validacion por campo

function validaNombre(){
    if ($("#elNombre").val().trim().length == 0) {
        mensajeError("eNombre","Debes ingresar tu nombre")
        return false
    } else {
        noError("eNombre")
        return true
    }
};
function validaEmail(){
    if ($("#elEmail").val().trim().length == 0) {
        mensajeError("eMail","Debes ingresar tu Email")
        return false
    } else {
        if (!esEmail($("#elEmail").val())) {
            mensajeError("eMail","formato Email NO valido")
            return false
        }else {
            noError("eMail")
            return true
        }
    }
};

function validaAsunto(){
    if ($("#elAsunto").val().trim().length == 0){
        mensajeError("eAsunto","Debes ingresar Asunto")
        return falso
    }else {
        noError("eAsunto")
        return true
    }
};

function validaMensaje(largo){
    if ($("#elMensaje").val().trim().length ==0){
        mensajeError("eMensaje","No ingresaste ningun mensaje")
        return false
    }else if ($("#elMensaje").val().trim().length < largo){
        mensajeError("eMensaje","El mensaje debe tener al menos "+ largo + " caracteres de largo")
        return false
    }else {
        noError("eMensaje")
        return true
    }
};

$(document).ready(function(){
    //mensajes error ocultos hasta ser invocados
    $(".invalid-feedback").hide();

    //cuando valida nombre?
    $("#elNombre").blur(function(){
        exito = validaNombre()
    });
    //cuando valida Email?
    $("#elEmail").blur(function(){
        exito = validaEmail()
    });
    //cuando valida asunto?
    $("#elAsunto").blur(function(){
        exito = validaAsunto()
    });
    //cuando se valida mensaje?
    $("#elMensaje").blur(function(){
        exito = validaMensaje()
    });
    $("#elMensaje").blur(function(){
        exito = validaMensaje(50)
    });
    $("#elMensaje").keyup(function(){
        var totalcaracteres = $("#elMensaje").val().trim().length
        $("#contcaract").text(totalcaracteres)
    });

    // cuando se activa el reset?
    $('button[type="reset"]').click(function(){
        $(".invalid-feedback").hide()
    });
    
    //checkea envio formulario

    $("#contactForm").submit(function(){
        exito = false

        if (
            !validaNombre(),
            !validaEmail(),
            !validaAsunto(),
            !validaMensaje()
        ) {
            e.preventDefault()
        }
    });
    
});
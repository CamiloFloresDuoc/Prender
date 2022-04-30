function validar() {
    var email, nombre, apellido, username, password, confirmpassword, expresion;
    email = document.getElementById("email").Value;
    nombre = document.getElementById("nombre").Value;
    apellido = document.getElementById("apellido").Value;
    username = document.getElementById("username").Value;
    password = document.getElementById("password").Value;
    confirmpassword = document.getElementById("confirmpassword").Value;
    //falta agarrar elemento del radio button!!!

    if (email === "" || nombre === "" || apellido === "" || username === "" || password === "" || confirmpassword === "") {
        alert("Todos los campos son obligatorios");
        return false;
    } else if (email.length > 100) {
        alert("El correo ingresado es muy largo");
        return false;

    } else if (nombre.length > 30) {
        alert("El nombre ingresado es muy Largo");
        return false;
    } else if (apellido.length > 30) {
        alert("El apellido ingresado es muy largo");
        return false;
    } else if (password.length < 6) {
        alert("La contraseña es muy corta, debe tener minimo 6 carácteres");
        return false;
    }

}

var check = function() {
    if (document.getElementById('password').value ==
      document.getElementById('confirmpassword').value) {
      document.getElementById('message').style.color = 'green';
      document.getElementById('message').innerHTML = 'Coinciden';
    } else {
      document.getElementById('message').style.color = 'red';
      document.getElementById('message').innerHTML = 'No coincide';
    }
  }
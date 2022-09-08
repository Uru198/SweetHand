var formLogin = document.getElementById('formLogin'); //Obteniedo el formulario
/* Vamos a escuchar cuando realice el evento ON SUBMIt */
var formLogin1 = document.getElementById('formLogin1');

formLogin.onsubmit = function(event) {
    event.preventDefault();

    //Creamos una variable con todos los datos del formulario
    var formulario = new FormData(formLogin)

    /* 
    formulario ={
        "email": "elena@coding.com",
        "password": "1234"
    }
    */

    fetch("/login", {method: 'POST', body: formulario})
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if(data.message == "correcto"){
                window.location.href = "/dashboard";
            }
            var mensajeAlerta = document.getElementById('mensajeAlerta'); // EL elemento con el id mensajeAlerta
            mensajeAlerta.innerText = data.message;
            mensajeAlerta.classList.add('alert');
            mensajeAlerta.classList.add('alert-danger');

        });

}

formLogin1.onsubmit = function(event) {
    event.preventDefault();

    //Creamos una variable con todos los datos del formulario
    var formulario = new FormData(formLogin1)

    /* 
    formulario ={
        "email": "elena@coding.com",
        "password": "1234"
    }
    */

    fetch("/registrate", {method: 'POST', body: formulario})

        .then(response => response.json())
        .then(data => {
            console.log(data)

            if(data.message == "correcto"){
                window.location.href = "/dashboard"  
            }
            
           
            
            var mensajeAlerta1 = document.getElementById('mensajeAlerta1'); // EL elemento con el id mensajeAlerta
            mensajeAlerta1.innerText = data.first_name;
            mensajeAlerta1.classList.add('alert');
            mensajeAlerta1.classList.add('alert-danger');
            

            var mensajeAlerta2 = document.getElementById('mensajeAlerta2'); // EL elemento con el id mensajeAlerta
            mensajeAlerta2.innerText = data.last_name;
            mensajeAlerta2.classList.add('alert');
            mensajeAlerta2.classList.add('alert-danger');

           
            var mensajeAlerta3 = document.getElementById('mensajeAlerta3'); // EL elemento con el id mensajeAlerta
            mensajeAlerta3.innerText = data.email;
            mensajeAlerta3.classList.add('alert');
            mensajeAlerta3.classList.add('alert-danger');

            if (data.password != null  && data.password != undefined) { 
            var mensajeAlerta4 = document.getElementById('mensajeAlerta4'); // EL elemento con el id mensajeAlerta
            mensajeAlerta4.innerText = data.password;
            mensajeAlerta4.classList.add('alert');
            mensajeAlerta4.classList.add('alert-danger');
            }
            if (data.confirm_password != null  && data.confirm_password != undefined) {
            var mensajeAlerta5 = document.getElementById('mensajeAlerta5'); // EL elemento con el id mensajeAlerta
            mensajeAlerta5.innerText = data.confirm_password;
            mensajeAlerta5.classList.add('alert');
            mensajeAlerta5.classList.add('alert-danger');
            }


        });

}
function filtrarVoluntario(caracter) {
    let voluntarios = document.querySelectorAll('.voluntario');

    voluntarios.forEach(function(voluntario){
        if (!(voluntario.getAttribute("nombreVoluntario").toLowerCase() + voluntario.getAttribute("apellidoVoluntario").toLowerCase()).includes(caracter.toLowerCase())) {
            voluntario.style.display = "none";
        }else{
            voluntario.style.display = "";
        }
    })
}

function confirmReiniciar(button, actividad){
    if (confirm("¿Estás seguro de que deseas reiniciar las inscripciones a la actividad " + actividad + "?")){
        button.parentNode.parentNode.submit();
    }
}

function eliminarVehiculo(button, patente){
    if (confirm("¿Estás seguro de que deseas eliminar el vehículo " + patente + "?")){
        button.parentNode.submit();
    }
}

function reiniciarVUCC(button){
    if (confirm("¿Deseas iniciar un nuevo ciclo del VUCC?\nEsto anulará todas las inscripciones a los voluntariados para dar inicio a un nuevo año de actividades dentro del VUCC.\nNo se eliminarán voluntarios ni voluntariados.")){
        button.parentNode.submit();
    }
}

function formatoURL(button, url){
    let subURL = url.split('/');
    let segmentoURL = subURL[4].split('-');
    let actionURL = "/password/reset/key/" + segmentoURL[0] + "-set-password/";
    let form = button.parentNode;

    form.action = actionURL;
    form.submit();
}

function cargarUsername(button){
    let username = document.getElementById("id_username");
    username.value = "default_user";
    let form = button.parentNode;
    button.style.display = 'none';
    form.submit();
}

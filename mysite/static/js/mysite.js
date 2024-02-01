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

function modificarVehiculo(button, patente){
    if (confirm("¿Estás seguro de que deseas modificar el vehículo " + patente + "?")){
        console.log(button.parentNode.parentNode);
        button.parentNode.parentNode.submit();
    }
}

function reiniciarVUCC(button){
    if (confirm("¿Deseas iniciar un nuevo ciclo del VUCC?\nEsto anulará todas las inscripciones a los voluntariados para dar inicio a un nuevo año de actividades dentro del VUCC.\nNo se eliminarán voluntarios ni voluntariados.")){
        button.parentNode.submit();
    }
}

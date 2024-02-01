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

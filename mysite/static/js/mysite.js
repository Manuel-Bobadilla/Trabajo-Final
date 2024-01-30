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

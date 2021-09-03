
if(  document.querySelector("#imagenPerfil") !== null){
  const $seleccionArchivos = document.querySelector("#imagenPerfil"),
  $imagenPrevisualizacion = document.querySelector("#profileImage");
  

$seleccionArchivos.addEventListener("change", () => {

  const archivos = $seleccionArchivos.files;

  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }

  const primerArchivo = archivos[0];

  const objectURL = URL.createObjectURL(primerArchivo);

  $imagenPrevisualizacion.src = objectURL;
  });
  
      
  document.getElementById("imagenPerfil").className += " form-control";
}else {

  const $seleccionArchivos = document.querySelector(".form-control-file"),
  $imagenPrevisualizacion = document.querySelector("#profileImage");
  

$seleccionArchivos.addEventListener("change", () => {

  const archivos = $seleccionArchivos.files;

  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }

  const primerArchivo = archivos[0];

  const objectURL = URL.createObjectURL(primerArchivo);

  $imagenPrevisualizacion.src = objectURL;
  });
  
      
  document.getElementsByClassName(".form-control-file").className += " form-control";
}


document.getElementsByClassName("text-truncate").className += " labelex";

//form-check-label

if(document.getElementById("id_imagen_perfil") !== null){
  document.getElementById("id_imagen_perfil").className += " form-control";
}



if(document.getElementById("id_estado")===null){

}else{
  document.getElementById("id_estado").className += " form-check-input";
}

if(document.getElementsByClassName("form-check-label")[0]){
  document.getElementsByClassName("form-check-label")[0].className += " form-check-label"
  document.getElementsByClassName("form-check-label")[0].innerHTML = "Alumno Activo";
}



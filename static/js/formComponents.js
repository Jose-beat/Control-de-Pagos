
if(  document.querySelector("#imagenPerfil") !== null){
  const $seleccionArchivos = document.querySelector("#imagenPerfil"),
  $imagenPrevisualizacion = document.querySelector("#profileImage");
  
// Escuchar cuando cambie
$seleccionArchivos.addEventListener("change", () => {
  // Los archivos seleccionados, pueden ser muchos o uno
  const archivos = $seleccionArchivos.files;
  // Si no hay archivos salimos de la función y quitamos la imagen
  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }
  // Ahora tomamos el primer archivo, el cual vamos a previsualizar
  const primerArchivo = archivos[0];
  // Lo convertimos a un objeto de tipo objectURL
  const objectURL = URL.createObjectURL(primerArchivo);
  // Y a la fuente de la imagen le ponemos el objectURL
  $imagenPrevisualizacion.src = objectURL;
  });
  
      
  document.getElementById("imagenPerfil").className += " form-control";
}else {
  //clearablefileinput form-control-file
  const $seleccionArchivos = document.querySelector(".form-control-file"),
  $imagenPrevisualizacion = document.querySelector("#profileImage");
  
// Escuchar cuando cambie
$seleccionArchivos.addEventListener("change", () => {
  // Los archivos seleccionados, pueden ser muchos o uno
  const archivos = $seleccionArchivos.files;
  // Si no hay archivos salimos de la función y quitamos la imagen
  if (!archivos || !archivos.length) {
    $imagenPrevisualizacion.src = "";
    return;
  }
  // Ahora tomamos el primer archivo, el cual vamos a previsualizar
  const primerArchivo = archivos[0];
  // Lo convertimos a un objeto de tipo objectURL
  const objectURL = URL.createObjectURL(primerArchivo);
  // Y a la fuente de la imagen le ponemos el objectURL
  $imagenPrevisualizacion.src = objectURL;
  });
  
      
  document.getElementsByClassName(".form-control-file").className += " form-control";
}


document.getElementsByClassName("text-truncate").className += " labelex";
if(document.getElementById("id_imagen_perfil") !== null){
  document.getElementById("id_imagen_perfil").className += " form-control";
}


if(  document.querySelector("#id_avatar") !== null){
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
  
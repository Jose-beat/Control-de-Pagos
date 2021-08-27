let alerta = document.getElementById("alerta");
alerta.addEventListener("click", ocultarRetraso)
let ocultarTiempo;


function ocultarRetraso(event){
     ocultarTiempo = setTimeout(ocultar, 500)
}

function ocultar (){
    console.log("Click")
    alerta.classList.add("ocultar")
    
   }
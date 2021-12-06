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

const splash = document.querySelector('.splash');

document.addEventListener('DOMContenLoaded', (e)=>{
    setTimeout( ()=>{
        splash.classList.add('display-none');
    }, 2000);
})

let cerrar = document.getElementById("cerrar");
let modal = document.getElementById("myModal");
let seleccionCobro = document.getElementById("SeleccionCobro");
let navegacion = document.getElementById("navegacion");

function abriModalVista(url){
    navegacion.style.zIndex = 0;
    
    var $ = jQuery.noConflict();

    $('#myModal').load(url, function(){
        $(this).modal('show');

    });
}

function cerrarModalVista(){
    navegacion.style.zIndex = 1;
    var $ = jQuery.noConflict();
        console.log("Cerrar")
        $('#myModal').modal('toggle');
     
     
}

function abriModal(url, modalName){
    navegacion.style.zIndex = 0;
    var $ = jQuery.noConflict();

    $(modalName).load(url, function(){
        $(this).modal('show');
        

    });
}

function cerrarModal(modalName){
    navegacion.style.zIndex = 1;
    var $ = jQuery.noConflict();
        console.log("Cerrar")
        $(modalName).modal('toggle');

    
     
}

function cambiarValor(modalName, idInput, valor){
    var $ = jQuery.noConflict();
        console.log("Cambio de valor: " + valor)
        console.log("Elemento a cambiar: " + idInput)
        
        $(idInput).val(valor)
        $(modalName).modal('toggle');
}
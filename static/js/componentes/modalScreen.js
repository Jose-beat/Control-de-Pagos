let cerrar = document.getElementById("cerrar");
let modal = document.getElementById("myModal");
let seleccionCobro = document.getElementById("SeleccionCobro")

function abriModalVista(url){

    var $ = jQuery.noConflict();

    $('#myModal').load(url, function(){
        $(this).modal('show');

    });
}

function cerrarModalVista(){
    var $ = jQuery.noConflict();
        console.log("Cerrar")
        $('#myModal').modal('toggle');
     
     
}

function abriModal(url, modalName){

    var $ = jQuery.noConflict();

    $(modalName).load(url, function(){
        $(this).modal('show');

    });
}

function cerrarModal(modalName){
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
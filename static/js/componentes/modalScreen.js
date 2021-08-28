let cerrar = document.getElementById("cerrar");
let modal = document.getElementById("myModal");

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
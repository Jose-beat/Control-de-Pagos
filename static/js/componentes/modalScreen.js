let cerrar = document.getElementById("cerrar");
let modal = document.getElementById("myModal");
let seleccionCobro = document.getElementById("SeleccionCobro");
let navegacion = document.getElementById("navegacion");
let main = document.getElementById("main");
let monto = 0;
let tramite = document.getElementById("tramite");

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
    main.style.zIndex = -1;
    var $ = jQuery.noConflict();

    $(modalName).load(url, function(){
        $(this).modal('show');
        

    });
}

function cerrarModal(modalName){
    navegacion.style.zIndex = 1;
    main.style.zIndex = 0;
    var $ = jQuery.noConflict();
        console.log("Cerrar")
        $(modalName).modal('toggle');

    
     
}

function cambiarValorAlumno(modalName, idInput, valor, valoresAlumno){
        var $ = jQuery.noConflict();
        console.log("Cambio de valor: " + valor)
        console.log("Elemento a cambiar: " + idInput)
        document.getElementById("matricula").innerHTML = valoresAlumno.matricula
        document.getElementById("nombreAlumno").innerHTML = valoresAlumno.nombre
        document.getElementById("apellidos").innerHTML = valoresAlumno.apellidos
        document.getElementById("domicilio").innerHTML = valoresAlumno.domicilio
        document.getElementById("carrera").innerHTML = valoresAlumno.carrera
        document.getElementById("telefono").innerHTML = valoresAlumno.telefono
        document.getElementById("email").innerHTML = valoresAlumno.email
        
        
        $('#id_descuento').val(valoresAlumno.descuento)
        let descuento = $('#id_descuento').val()
        console.log(document.getElementById('aplicaBeca'))
        if(document.getElementById('aplicaBeca').innerHTML !== null && document.getElementById('aplicaBeca').innerHTML !== "False"){
         if(descuento !== "0"){
                parseInt(descuento);
                let procentaje = descuento / 100;

                let totalDescuento = monto * procentaje;

                console.log("DESCUENTAZO: " + totalDescuento)
                total_sin_beca($('#id_cantidad').val(), monto)
                console.log("Antes del descuento " + $('#id_importe_total').val() )
                
                let total = $('#id_importe_total').val() - totalDescuento

                $('#id_importe_total').val(total)
            }else{
                total_sin_beca($('#id_cantidad').val(), monto)
            }
        }else{
            $('#id_descuento').val(0)
        }

        console.log(valoresAlumno)
     
        $(idInput).val(valor)
        cerrarModal(modalName)

}




function cambiarValorCobro(modalName, idInput, valor, valoresCobro){
    monto = valoresCobro.monto
    document.getElementById("idCobro").innerHTML = valoresCobro.idCobro
    document.getElementById("nombreCobro").innerHTML = valoresCobro.nombre
    document.getElementById("descripcion").innerHTML = valoresCobro.descripcion
    document.getElementById("monto").innerHTML = valoresCobro.monto
    document.getElementById("tipoCobro").innerHTML = valoresCobro.tipoCobro
    document.getElementById("aplicaBeca").innerHTML = valoresCobro.aplicaBeca
    asig_tramite()
    var $ = jQuery.noConflict();
  
    total_sin_beca($('#id_cantidad').val(), monto)
    console.log(valoresCobro)

    $(idInput).val(valor)
    cerrarModal(modalName)
}

function total_sin_beca(cantidad, monto){
    var $ = jQuery.noConflict();

    if(cantidad){
        let total = cantidad * monto
        $('#id_importe_total').val(total)
    }
}


function asig_tramite(){
    
    var $ = jQuery.noConflict();

    tramite.innerHTML = "N° " + $('#id_numero_tramite').val()
}

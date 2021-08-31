let cerrar = document.getElementById("cerrar");
let modal = document.getElementById("myModal");
let seleccionCobro = document.getElementById("SeleccionCobro");
let navegacion = document.getElementById("navegacion");
let main = document.getElementById("main");

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
        console.log(valoresAlumno)
        
        if(valoresAlumno.matricula){
            console.log("Hay un alumno")
        }else{
            console.log("no hay Alumno")   
        }

    

        $(idInput).val(valor)
        cerrarModal(modalName)
}


function cambiarValorCobro(modalName, idInput, valor, valoresCobro){
    document.getElementById("idCobro").innerHTML = valoresCobro.idCobro
    document.getElementById("nombreCobro").innerHTML = valoresCobro.nombre
    document.getElementById("descripcion").innerHTML = valoresCobro.descripcion
    document.getElementById("monto").innerHTML = valoresCobro.monto
    document.getElementById("tipoCobro").innerHTML = valoresCobro.tipoCobro

    var $ = jQuery.noConflict();

    console.log(valoresCobro)

    $(idInput).val(valor)
    cerrarModal(modalName)
}

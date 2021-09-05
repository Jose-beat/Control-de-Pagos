const cantidad = document.querySelector('#id_cantidad');
const descuentoTotal = document.querySelector('#id_descuento');
const importeTotal = document.querySelector('#id_importe_total');
let beca = document.getElementById('#aplicaBeca')

cantidad.addEventListener('change', (event) => {

    var $ = jQuery.noConflict();
    let cantidad = event.target.value;
    
    if(beca !== null && beca !== "False"){

        let descuento = $('#id_descuento').val()

        if(descuento !== "0"){
            parseInt(descuento);
                let procentaje = descuento / 100;

                let totalDescuento = monto * procentaje;

                console.log("DESCUENTAZO: " + totalDescuento)
                let total_sin_descuento = cantidad * monto
                $('#id_importe_total').val(total_sin_descuento)

                let total_con_descuento = $('#id_importe_total').val() - totalDescuento
                $('#id_importe_total').val(total_con_descuento)
                

        }else{
        let total_sin_descuento = cantidad * monto
        $('#id_importe_total').val(total_sin_descuento)
        }
    
    }else{
        $('#id_descuento').val(0)
    }
    
    
});


importeTotal.addEventListener('change', (event) => {
    var $ = jQuery.noConflict();
    let valor = event.target.value;
    console.log(valor)

});



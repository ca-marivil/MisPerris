$(document).ready(function() {

    $("#FormularioMascota").validate({
        rules:{

            txtnombre:{
                required: true,
                text:true
            },
            cbo_raza:{
                required: true
            },
            cbo_genero:{
                required: true
            },
            dpfecha_in:{
                required: true,
                number:true
            },
            dpfecha_nac:{
                required: true,
                number: true
            },
            cbo_estado:{
                required: true
            },
            txtimagen:{
                required: true
            }
        },
        messages:{
            txtnombre:{
                required:"Nombre No Ingresado",
                text:"Este campo solo acepta letras"
            },
            cbo_raza:{
                required:"Raza No Seleccionada"
            },
            cbo_genero:{
                required:"Genero No Seleccionado",
            },
            dpfecha_in:{
                required:"Fecha No Ingresada",
                number:"Este campo solo acepta numeros"
            },
            dpfecha_nac:{
                required:"Fecha No Ingresada",
                number:"Este campo solo acepta numeros"
            },
            cbo_estado:{
                required:"Estado No Seleccionado"

            },
            txtimagen:{
                required:"Imagen No Ingresada"
            }
        }
    });

});
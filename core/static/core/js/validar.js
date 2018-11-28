$(document).ready(function() {

    $("#FormularioCliente").validate({
        rules:{

            txtcorreo:{
                required: true
            },
            txtrun:{
                required: true,
                minlength:8,
                number:true
            },
            txtnombre:{
                required: true,
                text: true
            },
            dpfecha_Nac:{
                required: true,
                max:2001
            },
            txtnumero:{
                required: true,
                number: true

            },
            nomRegion:{
                required: true

            },
            nomComuna:{
                required: true
            },
            cbo_tipo_vivienda:{
                required: true
            }

        },
        messages:{
            txtcorreo:{
                required:"Correo No Ingresado"
            },
            txtrun:{
                required:"Rut No Ingresado",
                minlength:"Este campo no debe tener menos de 8 caracteres",
                number:"Este campo solo acepta numeros"
            },
            txtnombre:{
                required:"Nombre No Ingresado",
                text:"Este campo solo recibe caracteres"

            },
            dpfecha_Nac:{
                required:"Fecha No Ingresada",
                max:"La fecha de nacimiento no puede sobrepasar a 2001"
            },
            txtnumero:{
                required:"Numero De Contacto No Ingresado",
                number:"Este campo solo acepta numeros"
            },
            nomRegion:{
                required:"Escoja una opción"

            },
            nomComuna:{
                required:"Escoja una opción"
            },
            cbo_tipo_vivienda:{
                required:"Escoja una opción"
            }
        }
    });

});
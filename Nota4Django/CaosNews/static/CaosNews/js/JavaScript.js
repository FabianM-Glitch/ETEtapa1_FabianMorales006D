$(function() 
      {
        $("#mi-formulario").validate({
             rules: {
                    nombre: "required",
                    apellido: "required",
                    email: {
                        required: true,
                        email: true
                    },
                    telefono: "required",
                    direccion: "required",
                    combo: "required",
                    comentarios:"required",
                    
                }, //rules
            messages: {
                nombre:{
                    required: 'Debe ingresar su nombre'
                  },
                apellido:{
                    required: 'Debe ingresar su apellido'
                  },
                email: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                telefono:{
                    required: 'Ingrese un número de celular',
                    minlength: 'Cantidad de digitos insuficiente'
                },
                direccion:{
                    required:'Escriba su direccion',
                    minlength: 'Cantidad de digitos insuficiente'
                },
                combo:{
                    required:'Elija su combo'
                },
                comentarios:{
                required:'Debe escribir un comentario',
                minlength:'Cantidad de caracteres insuficiente'
                },
            }//messages
        }); //$('#mi-formulario').validate
    }); //function
/*Api */
    $(document).ready(function()
        {
            $("#enviar").click(function(){

                $.get("https://apis.digital.gob.cl/fl/feriados/2021",
                    function(data){
                        
                        $.each(data,function(i,item){
                            $("#fechas").append("<tr><td>"+item.nombre+"</td><td>"+item.fecha +
                            "</td><td>");
                            

                        });

                    });
            });
        })

        function CambiarMayusculas()
        {
            var a = document.getElementById("direccion");
            a.value = a.value.toUpperCase();
        }
        function MayusculaNombre()
        {
            var a = document.getElementById("nombre");
            a.value = a.value.charAt(0).toUpperCase()+a.value.substr (1);
        }

        function MayusculaApellido()
        {
            var a = document.getElementById("apellido");
            a.value = a.value.charAt(0).toUpperCase()+a.value.substr (1);
        }
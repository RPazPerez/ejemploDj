/**
* function login
*/
$(function(){$("#btn_login").click(function(){
    var user = $("#user").val();
    var password = $("#password").val();
    var token = $("input[name='csrfmiddlewaretoken']").val();
    if(user == ""){
      $("#user").addClass('error');
    }else{
      $("#user").removeClass('error');
    }
    if(password == ""){
      $("#password").addClass('error');
    }else{
      $("#password").removeClass('error');
    }
    if(user != "" && password != ""){
      $.ajax({
        url: 'login/autentificar',
        type: 'POST',
        data:{user:user, password:password, csrfmiddlewaretoken: token},
        success: function(data){
          if(data.mensaje == "Acceso"){
            window.location = "index";
          }else{
            alert("Usuario o Contraseña Incorrectos");
          }
        },
      });
    }
  });
});

/**
* function checked registro form
*
*/
function check_rabutton(elemento){
  if(elemento.name == "tipobano"){
    if(elemento.id == "banera"){
      $("#re").removeClass("radioseleccionado");
      $("#ba").addClass("radioseleccionado");
    }else{
      $("#re").addClass("radioseleccionado");
      $("#ba").removeClass("radioseleccionado");
    }
  }
  if(elemento.name == "tipoexcusado"){
    if(elemento.id == "noahorrador"){
      $("#noh").addClass("radioseleccionado");
      $("#ah").removeClass("radioseleccionado");
    }else{
      $("#noh").removeClass("radioseleccionado");
      $("#ah").addClass("radioseleccionado");
    }
  }
}

/**
* function registro
*
*/
$(function(){
  $("#btn_registro").click(function(){
    var token = $("input[name='csrfmiddlewaretoken']").val();
    var name = $('#name').val();
    var password = $('#password').val();
    var password_confirm = $('#password_confirm').val();
    var email = $('#email').val();
    if($("#banera").is(':checked')){ banera="SI"; }else{banera="NO";}
    if($("#regadera").is(':checked')){ regadera="SI"; }else{regadera="NO";}
    if($("#ahorrador").is(':checked')){ ahorrador="Ahorrador"; }else{ahorrador="NoAhorrador";}
    if(name != "" && password != "" && ahorrador != "" &&
        password_confirm != "" && email != "" && banera != "" && regadera != ""){
          if(password == password_confirm){
            $.ajax({
              url: 'registro/registrar',
              type: 'POST',
              data:{name:name, password:password, email:email, banera:banera, regadera:regadera, ahorrador:ahorrador, csrfmiddlewaretoken: token},
              success: function(data){
                console.log(data);
                if(data.mensaje == "Acceso"){
                  window.location = "/";
                }else{
                  alert("Usuario o Contraseña Incorrectos");
                }
              },
            });
          }else{
            alert("No coinciden las contraseñas");
          }
    }else{
      alert("Completar todos");
    }
  });
});

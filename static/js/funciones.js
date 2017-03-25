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

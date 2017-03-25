/**
* function login
*/
$(function(){$("#btn_login").click(function(){
    var email = $("#email").val();
    var password = $("#password").val();
    var token = $("#token").val();
    if(email == ""){
      $("#email").addClass('error');
    }else{
      $("#email").removeClass('error');
    }
    if(password == ""){
      $("#password").addClass('error');
    }else{
      $("#password").removeClass('error');
    }
    if(email != "" && password != ""){
      $.ajax({
        url: '/login',
        headers: {'X-CSRF-TOKEN': token},
        type: 'POST',
        dataType: 'json',
        data:{email:email, password:password},
        success: function(data){
          alert("Entro");
          console.log(data);
          if(data.mensaje == ""){
            window.location = "login";
          }
        },
        error: function(data){
          alert("error");
          console.log(data);
          // var errores = data.responseJSON;
          // $.each( errores, function( key, val ) {
          //     erroresAux = erroresAux+"@"+val;
          // });
          // self.errores(erroresAux);
        }
      });
    }
  });
});

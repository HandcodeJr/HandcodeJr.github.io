function sendMail(params){
  var temParams = {
      from_name: document.getElementById("name").value,
      to_name: 'HandCode',
      message: document.getElementById("message").value,
      reply_to: document.getElementById("email").value,
  };
  emailjs.send('service_veeelzl', 'template_kiwnh1p', temParams)
  .then(function(res){
    location.reload();
    alert("Email enviado!", res.status);
  })
}
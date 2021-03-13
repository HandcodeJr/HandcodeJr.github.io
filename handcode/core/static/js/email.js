function sendMail(params){
  var temParams = {
      from_name: document.getElementById("nome").value,
      to_name: 'HandCode',
      message: document.getElementById("menssagem").value,
      reply_to: document.getElementById("email").value,
  };
  emailjs.send('service_no0hf5e', 'template_idfhjxi', temParams)
  .then(function(res){
    location.reload();
    alert("Email enviado!", res.status);
  })
}
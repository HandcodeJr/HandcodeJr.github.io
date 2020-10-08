from django.shortcuts import render
from django.contrib import messages
from django.core.mail.message import EmailMessage

def home(request):
    def send_mail(self):
            nome = self.cleaned_data['nome']
            email = self.cleaned_data['email']
            assunto = self.cleaned_data['assunto']
            mensagem = self.cleaned_data['mensagem']

            conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto; {assunto}\nMensagem: {mensagem}'
            
            mail = EmailMessage(
                subject = assunto,
                body =conteudo,
                from_email = handcodeej@gmail.com 
                headers ={'Reply-to': email}
            )

    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

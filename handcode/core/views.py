from django.shortcuts import render
from django.contrib import messages
from django.core.mail.message import EmailMessage

from .models import Worker

def home(request):  
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    worker = Worker.objects.order_by('?').all()
    data = {
        'worker': worker,
    }
    return render(request,'team.html', data)
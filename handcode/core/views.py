from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

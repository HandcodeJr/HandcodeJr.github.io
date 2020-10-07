from django.urls import path

from core.views import home,contact,about,services,team

urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('team', team,  name='team'),
]   
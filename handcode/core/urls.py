from django.urls import path

from core.views import home,about,services,team

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('team', team,  name='team'),
]   
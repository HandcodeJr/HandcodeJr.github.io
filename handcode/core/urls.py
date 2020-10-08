from django.urls import path

from .views import home,contact,about,services,team

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
    path('sobre-nos/', about, name='about'),
    path('servicos/', services, name='services'),
    path('equipe/', team,  name='team'),
]
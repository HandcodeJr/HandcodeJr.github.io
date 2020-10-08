from django.urls import path

<<<<<<< HEAD
from core.views import home,about,services,team

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('team', team,  name='team'),
]   
=======
from .views import home,contact,about,services,team

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
    path('sobre-nos/', about, name='about'),
    path('servicos/', services, name='services'),
    path('equipe/', team,  name='team'),
]
>>>>>>> 80c0bab0f7c54c0de0b258d04a861774fae16cb1

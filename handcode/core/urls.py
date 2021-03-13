from django.urls import path

from .views import home,about,services,team,notFound

urlpatterns = [
    path('', home, name='home'),
    path('sobre-nos/', about, name='about'),
    path('servicos/', services, name='services'),
    path('equipe/', team,  name='team'),
    
    path('notfound/', notFound,  name='notFound'),
    
]

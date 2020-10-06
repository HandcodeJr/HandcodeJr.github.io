from django.urls import path

from core.views import home,contact,about,services,team

urlpatterns = [
    path('', home),
    path('contact', contact),
    path('about', about),
    path('services', services),
    path('team', team),
]   
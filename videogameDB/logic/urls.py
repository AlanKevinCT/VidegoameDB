from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_Videogames, name='listar_videojuegos'),
    path('agregar/', views.agregar_Videogame, name='agregar_videojuego'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.enlist, name='listar_videojuegos'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('', enlist, name='enlist_vg'),
    path('add/', AddVideogame.as_view(), name='add_vg'),
    path('rm/<int:id_game>', delete, name='rm_vg'),
]
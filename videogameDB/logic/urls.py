from django.urls import path
from . import views

urlpatterns = [
    path('', views.enlist, name='enlist_vg'),
]
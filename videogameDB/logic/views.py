from django.shortcuts import render
from .models import Videogame

def enlist(request):
    games = Videogame.objects.all()
    return render(request, 'enlist.html', {'games': games})

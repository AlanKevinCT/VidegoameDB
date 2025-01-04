from django.shortcuts import render,redirect, get_object_or_404
from rest_framework.views import APIView
from .models import Videogame
from .forms import Form

def enlist(request):
    games = Videogame.objects.all()
    return render(request, 'enlist.html', {'games': games})

class AddVideogame(APIView):
    def get(self, request):
        form = Form()
        return render(request, 'add-form.html', {'form': form})
    
    def post(self, request):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enlist_vg')
        return render(request, 'add-form.html', {'form': form})
    
def delete(request, id_game):
    videogame = get_object_or_404(Videogame, pk=id_game)
    videogame.delete()
    return redirect('enlist_vg')
from django.http import HttpResponseNotAllowed
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
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enlist_vg')
        return render(request, 'add-form.html', {'form': form})
    
def delete(request, id_game):
    videogame = get_object_or_404(Videogame, pk=id_game)
    videogame.delete()
    return redirect('enlist_vg')

class PatchVideogame(APIView):
    def get(self, request, id_game):
        videogame = get_object_or_404(Videogame, pk=id_game)
        form = Form(instance=videogame)
        return render(request, 'edit-form.html', {'form': form, 'videogame': videogame})
    
    def post(self, request, id_game):
        if request.POST.get('_method') == 'PATCH':
            videogame = get_object_or_404(Videogame, pk=id_game)
            form = Form(request.POST, instance=videogame)
            if form.is_valid():
                form.save()
                return redirect('enlist_vg')
            return render(request, 'edit-form.html', {'form': form, 'videogame': videogame})
        else:
            return HttpResponseNotAllowed(['PATCH'])
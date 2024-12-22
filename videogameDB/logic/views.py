from django.shortcuts import render
from .models import Videogame

def listar_Videogames(request):
    juegos = Videogame.objects.all()
    return render(request, 'listar_Videogames.html', {'juegos': juegos})


from django.shortcuts import render, redirect
from .models import Videogame

def agregar_Videogame(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        plataforma = request.POST.get('plataforma')
        fecha_lanzamiento = request.POST.get('fecha_lanzamiento')

        # Crear un nuevo Videogame
        Videogame.objects.create(
            nombre=nombre,
            plataforma=plataforma,
            fecha_lanzamiento=fecha_lanzamiento
        )
        return redirect('listar_Videogames')
    return render(request, 'agregar_Videogame.html')

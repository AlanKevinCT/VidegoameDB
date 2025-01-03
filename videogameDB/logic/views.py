from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
        if request.content_type == 'application/json':
            form = Form(request.data)
            if form.is_valid():
                form.save()
                return Response({"message": "Videogame created successfully"}, status=status.HTTP_201_CREATED)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            form = Form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('enlist_vg')
            return render(request, 'add-form.html', {'form': form})
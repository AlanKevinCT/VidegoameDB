from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Videogame
from .serializers import Serializer

def enlist(request):
    games = Videogame.objects.all()
    return render(request, 'enlist.html', {'games': games})

class AddVideogame(APIView):
    def post(self, request):
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
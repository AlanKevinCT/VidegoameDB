from django.db import models

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    plataforma = models.CharField(max_length=50)

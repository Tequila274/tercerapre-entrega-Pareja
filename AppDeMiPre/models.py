from django.db import models


# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    rol = models.CharField(max_length=20)
    def __str__(self):
        
        return f"Nombre: {self.nombre} rol: {self.rol}"
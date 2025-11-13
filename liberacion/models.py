from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='estudiante', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    nivel_ingles = models.CharField(max_length=50)
    fecha_liberacion = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.matricula})"



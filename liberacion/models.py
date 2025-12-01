from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    nivel_ingles = models.CharField(max_length=10)
    boleta = models.FileField(upload_to='boletas/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ Campos nuevos para la firma


    firmado = models.BooleanField(default=False)
    fecha_firma = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.matricula}"




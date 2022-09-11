from django.db import models
from django.contrib.auth.models import User #Buscar para que es
#User._meta.get_field('email')._unique = True


# Create your models here.

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    cod_estudiante = models.CharField(max_length=12)
    acudiente = models.CharField(max_length=180)
    telefono = models.CharField(max_length=14, blank=True)
    direccion = models.CharField(max_length=50, blank=True)

class Programa(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(blank=True)

class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    cod_profesor = models.CharField(max_length=12)
    telefono = models.CharField(max_length=14)
    direccion = models.CharField(max_length=50, blank=True)

class Materia(models.Model):
    Programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)

class Seguimiento(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True)

class LogAuditor(models.Model):
    mensajeError = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
from django.db import models

# Create your models here.
class Arrendatario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.TextField(max_length=150)
    lugar_arrendar = models.TextField(max_length=150)

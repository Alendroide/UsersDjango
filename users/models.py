from django.db import models

# Create your models here.
class Persona(models.Model):
    estados = [('activo','Activo'),('inactivo','Inactivo')]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=100,choices=estados,default='activo')
    fechaCreacion = models.DateField(auto_now=True)
    def __str__(self):
        return self.nombre
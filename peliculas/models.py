from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre 

class Pelicula (models.Model):
    nombre = models.CharField(max_length=80)
    sinopsis = models.TextField()
    anio   = models.IntegerField()
    productor = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, related_name='pelicula', on_delete=models.CASCADE) 
    fecha_Creacion = models.DateTimeField('Creado',
            default=timezone.now)
    
    def publish(self):
        self.fecha_Creacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre
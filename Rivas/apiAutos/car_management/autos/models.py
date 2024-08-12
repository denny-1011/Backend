from django.db import models
from marcas.models import Marca
from modelos.models import Modelo

class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    inventario = models.IntegerField()
    nombre = models.CharField(max_length=255, default='Auto por defecto')
    imagen = models.CharField(max_length=255, null=True, blank=True)  
    imagenprev = models.CharField(max_length=255, null=True, blank=True)  

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

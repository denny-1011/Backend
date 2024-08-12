from django.db import models
from autos.models import Auto

class Inventario(models.Model):
    auto = models.OneToOneField(Auto, on_delete=models.CASCADE, related_name='inventario_detalle')
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Inventario de {self.auto}"

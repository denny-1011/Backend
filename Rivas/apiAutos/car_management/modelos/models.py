from django.db import models

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey('marcas.Marca', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.nombre}"

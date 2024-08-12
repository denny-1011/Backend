from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    sucursal = models.ForeignKey('sucursales.Sucursal', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

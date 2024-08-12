from django.db import models
from autos.models import Auto
from clientes.models import Cliente

class ServicioPostVenta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_servicio = models.DateTimeField(auto_now_add=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Servicio post-venta de {self.auto} para {self.cliente}"

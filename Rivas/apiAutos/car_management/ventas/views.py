from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Venta
from .serializers import VentaSerializer

class VentasViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cliente', 'vendedor', 'precio', 'fecha']


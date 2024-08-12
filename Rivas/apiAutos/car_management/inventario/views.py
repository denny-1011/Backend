from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Inventario
from .serializers import InventarioSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cantidad']


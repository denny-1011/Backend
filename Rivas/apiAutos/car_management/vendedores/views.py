from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Vendedor
from .serializers import VendedorSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sucursal']


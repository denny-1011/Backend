from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Sucursal
from .serializers import SucursalSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    filter_backends = [DjangoFilterBackend]


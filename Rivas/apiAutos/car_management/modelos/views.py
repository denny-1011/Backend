from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Modelo
from .serializers import ModeloSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['marca']


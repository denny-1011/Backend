from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Auto
from .serializers import AutoSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['marca', 'modelo', 'año', 'precio']



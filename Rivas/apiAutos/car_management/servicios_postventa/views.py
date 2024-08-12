from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import ServicioPostVenta
from .serializers import ServiciosSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = ServicioPostVenta.objects.all()
    serializer_class = ServiciosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['costo']


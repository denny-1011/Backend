from rest_framework import serializers
from .models import ServicioPostVenta

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioPostVenta
        fields = '__all__'




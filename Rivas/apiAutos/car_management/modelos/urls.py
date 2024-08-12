from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModeloViewSet

router = DefaultRouter()
router.register(r'modelos', ModeloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

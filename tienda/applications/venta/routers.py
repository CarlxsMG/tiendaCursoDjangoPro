# Django Rest Framework imports
from rest_framework.routers import DefaultRouter

# Local imports
from . import viewsets


# Code
router = DefaultRouter()
router.register(r'ventas', viewsets.VentasViewSet, basename="ventas")

urlpatterns = router.urls

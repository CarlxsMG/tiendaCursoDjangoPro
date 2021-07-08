# Django Rest Framework imports
from rest_framework.routers import DefaultRouter

# Local imports
from . import viewsets


# Code
router = DefaultRouter()
router.register(r'colors', viewsets.ColorViewSet, basename="colors")
router.register(r'productos', viewsets.ProductViewSet, basename="productos")

urlpatterns = router.urls

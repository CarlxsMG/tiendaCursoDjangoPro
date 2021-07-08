# Django Rest Framework imports
from rest_framework.routers import DefaultRouter

# Local imports
from . import viewsets


# Code
router = DefaultRouter()
router.register(r'colors', viewsets.ColorViewSet, basename="colors")

urlpatterns = router.urls

# Django Rest Framework imports
from rest_framework import viewsets

# Local imports
from .models import Colors
from .serializers import ColorSerializer


# Code

class ColorViewSet(viewsets.ModelViewSet): # ESTO ES UN CRUD
    serializer_class = ColorSerializer # Requerido por el ViewSet
    queryset = Colors.objects.all()    # Requerido por el ViewSet
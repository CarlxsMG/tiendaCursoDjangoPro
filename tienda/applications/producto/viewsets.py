# Django Rest Framework imports
from rest_framework import viewsets

# Local imports
from .models import Colors, Product
from .serializers import (
    ColorSerializer,
    ProductSerializer,
    PaginationSerializer,
    ProductSerializerViewSets
)


# Code

class ColorViewSet(viewsets.ModelViewSet): # ESTO ES UN CRUD
    serializer_class = ColorSerializer # Requerido por el ViewSet
    queryset = Colors.objects.all()    # Requerido por el ViewSet


class ProductViewSet(viewsets.ModelViewSet): # ESTO ES UN CRUD
    serializer_class = ProductSerializerViewSets # Requerido por el ViewSet
    queryset = Product.objects.all()    # Requerido por el ViewSet

    pagination_class = PaginationSerializer
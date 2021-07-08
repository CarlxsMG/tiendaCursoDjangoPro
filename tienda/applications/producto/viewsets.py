# Django Rest Framework imports
from rest_framework import viewsets
from rest_framework.response import Response

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


    def perform_create(self, serializer):

        if str(serializer.validated_data['video']) == "":
            serializer.validated_data['video'] = "https://www.youtube.com/"

        serializer.save(
            video=serializer.validated_data['video']
        )

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def list(self,request,*args, **kwargs):
        queryset = Product.objects.productos_por_user(self.request.user)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
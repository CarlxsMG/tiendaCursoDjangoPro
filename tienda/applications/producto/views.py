# Django imports
from django.shortcuts import render

# Django Rest Framework imports
from rest_framework.generics import(
    ListAPIView,
)

# Local imports
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
# Django imports
from django.shortcuts import render

# Django Rest Framework imports
from rest_framework.generics import(
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local imports
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,) #Descifra e identifica al usuario
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Recuperar usuario
        user = self.request.user
        return Product.objects.productos_por_user(user)
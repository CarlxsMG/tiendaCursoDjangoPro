# Django Rest Framework imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local imports
from .serializers import ProcesoVentaSerializer2, VentaReporteSerializers
from .models import Sale, SaleDetail
from applications.producto.models import Product


# Code
class VentasViewSet(viewsets.ViewSet):
    serializer_class = ProcesoVentaSerializer2
    queryset = Sale.objects.all()
    
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    def list(self, request): # Requerido para el viewsets.ViewSet
        return Response({'ok':'ok'})

    def retrieve(self, request, pk=None): # Requerido para el viewsets.ViewSet
        return Response({'ok':'ok2'})
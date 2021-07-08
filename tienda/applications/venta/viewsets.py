# Python imports
from django.utils.timezone import now

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
    queryset = Sale.objects.all()
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def list(self, request): # Requerido para el viewsets.ViewSet
        queryset = Sale.objects.all()
        serializer = VentaReporteSerializers(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, pk=None): # opcional para el viewsets.ViewSet
        serializer = ProcesoVentaSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # recuperar productos de una venta
        products = Product.objects.filter(
            id__in=serializer.validated_data['productos']
        )

        cantidades = serializer.validated_data['cantidades']
        
        venta = Sale.objects.create(
            date_sale=now(),
            amount=0,
            count=0,
            type_invoce=serializer.validated_data['type_invoce'],
            type_payment=serializer.validated_data['type_payment'],
            adreese_send=serializer.validated_data['adreese_send'],
            user=self.request.user,
        )

        # Variables from ventas
        amount, count = 0,0
        
        ventas_detalle = []

        for producto, cantidad in zip(products, cantidades):

            venta_detalle = SaleDetail(
                sale=venta,
                product=producto,
                count=cantidad,
                price_purchase=producto.price_purchase,
                price_sale=producto.price_sale
            )

            ventas_detalle.append(venta_detalle)

            amount = amount + (producto.price_sale * cantidad)
            count = count + cantidad

        venta.amount = amount
        venta.count = count
        venta.save()

        SaleDetail.objects.bulk_create(ventas_detalle)

        return Response(serializer.data)

    def retrieve(self, request, pk=None): # Requerido para el viewsets.ViewSet
        return Response({'ok':'ok2'})

    def update(self, request, pk=None): # opcional para el viewsets.ViewSet
        return Response({'ok':'ok3'})

    def destroy(self, request, pk=None): # opcional para el viewsets.ViewSet
        return Response({'ok':'ok5'})
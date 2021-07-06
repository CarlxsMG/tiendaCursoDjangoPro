# Django imports
from django.shortcuts import render
from django.utils.timezone import now

#Django Rest Framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Local imports
from .models import Sale, SaleDetail
from applications.producto.models import Product
from .serializers import (
    VentaReporteSerializers,
    ProcesoVentaSerializer,
    ProcesoVentaSerializer2,
)
from applications.venta import serializers

# Create your views here.
class ReporteVentasList(ListAPIView):

    serializer_class = VentaReporteSerializers

    def get_queryset(self):
        return Sale.objects.all()


class ReporteVentasList(ListAPIView):

    serializer_class = VentaReporteSerializers

    def get_queryset(self):
        return Sale.objects.all()

class RegistrarVenta(CreateAPIView):
    ''' View to register sell '''

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]

    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # type_invoce = serializer.validated_data['type_invoice'] # This need before to work | serializer.is_valid(raise_exception=True)
        
        # recuperar productos de una venta
        products = serializer.validated_data['productos']
        
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
        amount, count = 0
        
        ventas_detalle = []

        for producto in products:
            # get pk of product to post
            prod = Product.objects.get(id=producto['pk'])

            venta_detalle = SaleDetail(
                sale=venta,
                product=prod,
                count=producto['count'],
                price_purchase=prod.price_purchase,
                price_sale=prod.price_sale
            )

            ventas_detalle.append(venta_detalle)

            amount = amount + (prod.price_sale * producto['count'])
            count = count + producto['count']

        venta.amount = amount
        venta.count = count
        venta.save()

        SaleDetail.objects.bulk_create(ventas_detalle)

        return Response({'code':'ok'})



class RegistrarVenta2(CreateAPIView):
    ''' View to register sell '''

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    serializer_class = ProcesoVentaSerializer2

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer2(data=request.data)
        serializer.is_valid(raise_exception=True)

        # type_invoce = serializer.validated_data['type_invoice'] # This need before to work | serializer.is_valid(raise_exception=True)
        
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

        return Response({'code':'ok'})
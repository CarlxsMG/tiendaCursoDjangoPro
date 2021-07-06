# Django Rest Framework imports
from rest_framework import serializers

# Local imports
from .models import Sale, SaleDetail


class VentaReporteSerializers(serializers.ModelSerializer):
    ''' Serializador para ver las ventas en detalle '''

    products = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'id',
            'date_sale',
            'amount',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state','adreese_send',
            'user',
            'products'
        )

    def get_products(self, obj): # Necesario para el MethodField // Object en el modelo Sale
        
        sale_detail = SaleDetail.objects.productos_por_venta(obj.id)

        products_serialized = DetalleVentaProductoSerializer(sale_detail, many=True).data

        return products_serialized



class DetalleVentaProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SaleDetail
        fields = (
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale',
        )


class ProductDetailSerializer(serializers.Serializer):

    pk = serializers.IntegerField()
    count = serializers.IntegerField()


class ProcesoVentaSerializer(serializers.Serializer):

    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()

    productos = ProductDetailSerializer(many=True)


class ArrayIntegerSerializer(serializers.ListField):

    child = serializers.IntegerField()


class ProcesoVentaSerializer2(serializers.Serializer):

    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()

    productos = ArrayIntegerSerializer()
    cantidades = ArrayIntegerSerializer()
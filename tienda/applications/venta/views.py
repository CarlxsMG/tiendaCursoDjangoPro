# Django imports
from django.shortcuts import render

#Django Rest Framework
from rest_framework.generics import (
    ListAPIView
)

# Local imports
from .models import Sale
from .serializers import VentaReporteSerializers

# Create your views here.
class ReporteVentasList(ListAPIView):

    serializer_class = VentaReporteSerializers

    def get_queryset(self):
        return Sale.objects.all()
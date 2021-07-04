# Django imports
from django.urls import path, include

# Local imports
from . import views

app_name='producto_app'

urlpatterns = [
    path('api/product/por-usuario/', views.ListProductUser.as_view(), name='product-producto_by_user'),

    path('api/product/por-stok/', views.ListProductStok.as_view(), name='product-producto_by_stok'),
    
    path('api/product/por-genero/<gender>/', views.ListProductGenero.as_view(), name='product-producto_by_genero'),
]

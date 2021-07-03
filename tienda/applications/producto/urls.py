# Django imports
from django.urls import path, include

# Local imports
from . import views

app_name='producto_app'

urlpatterns = [
    path('api/product/por-usuario/', views.ListProductUser.as_view(), name='product-producto_by_user')
]

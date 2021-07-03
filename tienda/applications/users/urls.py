# Django imports
from django.contrib import admin
from django.urls import path

# Local views
from . import views

app_name = 'users_app'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
]

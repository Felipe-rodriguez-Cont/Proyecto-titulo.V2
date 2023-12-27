from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('cliente/', views.cliente_views, name='clienteViews' ),
        
]

from django import views
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('ventas/', views.ventas_views, name= 'ventas'),
    path('clientes/', views.clientes_views, name= 'clientes'),
    path('add_clientes/', views.add_clientes_views, name= 'AddCliente'),
    path('edit_clientes/', views.edit_clientes_views, name= 'EditCliente'),
    path('delete_clientes/', views.delete_clientes_views, name= 'DeleteCliente'),
    
]

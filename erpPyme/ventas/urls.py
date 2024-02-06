from django import views
from django.contrib import admin
from django.urls import URLPattern, include, path
from . import views


urlpatterns = [
    path('ventas/', views.ventas_views, name= 'ventas'),
    path('clientes/', views.clientes_views, name= 'clientes'),
    path('add_clientes/', views.add_clientes_views, name= 'AddCliente'),
    path('edit_clientes/', views.edit_clientes_views, name= 'EditCliente'),
    path('delete_clientes/', views.delete_clientes_views, name= 'DeleteCliente'),
    path('productos/', views.productos_view, name= 'productos'),
    path('add_productos/', views.add_productos_views, name= 'AddProducto'),
    path('edit_productos/', views.edit_producto_views, name= 'EditProducto'),
    #path('delete_productos/', views.delete_productos_views, name= 'DeleteProductos'),
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
    
]

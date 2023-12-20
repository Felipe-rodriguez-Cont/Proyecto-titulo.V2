from django.urls import path
from erp.views import *

urlpatterns = [
    path('prueba/', pruebaPagina, name= "prueba"),
]

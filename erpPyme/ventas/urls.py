from django import views
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('ventas/', views.ventas_views, name= 'ventasViews'),
    
]

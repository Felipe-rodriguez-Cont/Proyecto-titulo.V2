from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def pruebaPagina(request):
    return HttpResponse ('hola prueba de first page')

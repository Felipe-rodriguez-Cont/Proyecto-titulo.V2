from django.shortcuts import render

# Create your views here.
def ventas_views (request):
    return render(request, 'ventas/ventas.html')
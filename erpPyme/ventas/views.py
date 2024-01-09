from django.shortcuts import render, redirect
from .models import Cliente, producto
from .forms import *
from django.contrib import messages

# Create your views here.
def ventas_views (request):
    num_ventas =  156
    context = {
        'num_ventas': num_ventas
    }
    return render(request, 'ventas/ventas.html', context)

def clientes_views (request):
    clientes = Cliente.objects.all()
    form_personal = addClienteForm()
    form_editar = editarClienteForm()
    context = {  
               'clientes': clientes,
               'form_personal' : form_personal,
               'form_editar' : form_editar,
    }
    return render(request, 'clientes/clientes.html', context)

def add_clientes_views (request):
    print('guardar cliente')
    if request.POST:
        form = addClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages (request,"Error al guardar cliente")
                return redirect('clientes')
    return redirect ('clientes')

def edit_clientes_views (request):
    if request.POST:
        cliente=Cliente.objects.get(pk = request.POST.get('id_personal_editar') )
        form=editarClienteForm(
            request.POST,request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
    return redirect ('clientes')

def delete_clientes_views (request):
    if request.POST:
        cliente = Cliente.objects.get(pk = request.POST.get('id_personal_eliminar') )
        cliente.delete()
        
    return redirect ('clientes')

# def productos (request):
#     clientes = Cliente.objects.all()
#     form_personal = addClienteForm()
#     form_editar = editarClienteForm()
#     context = {  
#                'clientes': clientes,
#                'form_personal' : form_personal,
#                'form_editar' : form_editar,
#     }
#     return render(request, 'productos/productos.html', context)
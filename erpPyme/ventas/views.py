from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from .models import Cliente, Egreso, Producto, Egreso, ProductosEgreso
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os

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
        if form.is_valid():
            try:
                form.save()
            except:
                messages.error(request, "Error al guardar cliente")
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

def productos_view (request):
    productos = Producto.objects.all()
    form_add = addProductoForm()
    form_editar = editarProductoForm()
   
    context = {  
               'productos': productos,
               'form_add' : form_add,
               'form_editar' : form_editar,
    }
    return render(request, 'productos/productos.html', context)

def add_productos_views (request):
    
    print('guardar producto')
    if request.POST:
        form = addProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages.error(request, "Error al guardar el Producto")
                return redirect('productos')
    return redirect ('productos')

def edit_producto_views (request):
    if request.POST:
        producto =Producto.objects.get(pk = request.POST.get('id_producto_editar') )
        form=editarProductoForm(
            request.POST,request.FILES, instance= producto)
        if form.is_valid():
            form.save()
    return redirect ('productos')

class add_ventas(ListView):
    template_name = 'ventas/add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)


def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket/ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Mi empresa S.A. De C.V"
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response
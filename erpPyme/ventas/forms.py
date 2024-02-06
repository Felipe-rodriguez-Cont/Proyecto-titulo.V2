from django import forms
from ventas.models import Cliente, Producto

class addClienteForm(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo Cliente: ',
            'nombre': 'Nombre cliente',
            'telefono':'Telefono - Contacto'
        }
        
class editarClienteForm(forms.ModelForm):
     class Meta: 
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Codigo Cliente: ',
            'nombre': 'Nombre cliente',
            'telefono':'Telefono - Contacto'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id':'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id':'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }
        
class addProductoForm(forms.ModelForm):
    class Meta: 
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen', 'costo', 'cantidad', 'precio')
        labels = {
            'codigo': 'Codigo Producto: ',
            'descripcion': 'Descripcion Producto',
            'imagen': 'Imagen Producto',
            'costo': 'Costo Producto',
            'cantidad': 'Cantidad',
            'precio': 'Precio ',
        }
        
class editarProductoForm(forms.ModelForm):
     class Meta: 
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen', 'costo','precio','cantidad')
        labels = {
            'codigo': 'Codigo Producto: ',
            'descripcion': 'Descripcion Producto',
            'imagen': 'Imagen Producto',
            'costo': 'Costo Producto',            
            'precio': 'Precio ',
            'cantidad': 'Cantidad',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id':'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id':'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id': 'costo_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_editar'})
        }
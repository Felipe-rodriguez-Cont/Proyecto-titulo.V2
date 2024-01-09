from django import forms
from ventas.models import Cliente

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
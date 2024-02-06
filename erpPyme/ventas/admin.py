from django.contrib import admin
from ventas.models import Cliente,Producto

# Register your models here.
class clienteAdmin(admin.ModelAdmin):
    list_display= ('nombre','telefono','codigo')
    search_fields = ['nombre']
    readonly_fields = ('created','updated')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register (Cliente,clienteAdmin)
class productoAdmin(admin.ModelAdmin):
    list_display= ('descripcion','cantidad','costo')
    search_fields = ['descripcion']
    readonly_fields = ('created','updated')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register (Producto,productoAdmin)
    


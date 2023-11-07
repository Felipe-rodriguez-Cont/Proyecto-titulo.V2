from django.db import models
from datetime import datetime

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Nombre'
        verbose_name_plural ='Nombres'
        ordering = ['id']

class category (models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural ='categorias'
        ordering = ['id']
   
class Employe (models.Model):
    categ = models.ManyToManyField(category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE )
    names = models.CharField(max_length=150, verbose_name= "Nombres")
    dni = models.CharField(max_length=10 , verbose_name= "Dni", unique=True)
    date_joined = models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField(default=0)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar', null=True , blank= True)
    cv = models.FileField(upload_to='cvitae', null=True , blank= True)
    
    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
        

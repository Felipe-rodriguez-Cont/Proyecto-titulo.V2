from django.db import models

# Create your models here.

class usuario(models.Model):
    #creamos un id con numeros consecutivos y con llave primaria.
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return str(self.id)
    
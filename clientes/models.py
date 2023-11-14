from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre_cliente=models.CharField( max_length=40)
    nombre_popriedad=models.CharField( max_length=80)
    num_inmuebles=models.IntegerField()
    años_antiguedad=models.IntegerField()
    saldo_cartera=models.IntegerField()
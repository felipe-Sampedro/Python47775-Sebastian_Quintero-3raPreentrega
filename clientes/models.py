from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre_cliente=models.CharField(max_length=40)
    nombre_popriedad=models.CharField(max_length=80)
    num_inmuebles=models.IntegerField()
    años_antiguedad=models.IntegerField()
    saldo_cartera=models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.nombre_cliente} - {self.num_inmuebles} - {self.años_amtoguedad} - {self.saldo_cartera}'
    
class Propiedad(models.Model):
    tipo=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=250)
    num_habitaciones=models.IntegerField()
    area_total_m2=models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.tipo} - {self.num_habitaciones} - {self.area_total_m2}'
    
class Cartera(models.Model):
    cliente=models.CharField(max_length=40)
    estado=models.CharField(max_length=10)
    saldo=models.IntegerField()
    dias_mora=models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.cliente} - {self.estado} - {self.saldo} - {self.dias_mora}'
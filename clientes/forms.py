from django import forms

class Crear_cliente(forms.Form):
    num_doc=forms.IntegerField()
    nombre_cliente=forms.CharField(max_length=40)
    nombre_popriedad=forms.CharField(max_length=80)
    num_inmuebles=forms.IntegerField()
    anios_antiguedad=forms.IntegerField()
    saldo_cartera=forms.IntegerField()

class Crear_propiedad(forms.Form):
    ref_prop=forms.IntegerField()
    tipo=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=250)
    num_habitaciones=forms.IntegerField()
    area_total_m2=forms.IntegerField()
    
class Crear_cartera(forms.Form):
    num_doc=forms.IntegerField()
    cliente=forms.CharField(max_length=40)
    estado=forms.CharField(max_length=10)
    saldo=forms.IntegerField()
    dias_mora=forms.IntegerField()
    
    
class Buscar_cliente(forms.Form):
    nombre_cliente=forms.CharField(max_length=40)
 
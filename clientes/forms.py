from django.forms import forms

class Clientes(forms.Form):
    nombre_cliente=forms.CharField( max_length=40)
    nombre_popriedad=forms.CharField( max_length=80)
    num_inmuebles=forms.IntegerField()
    años_antiguedad=forms.IntegerField()
    saldo_cartera=forms.IntegerField()

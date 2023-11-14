from django.shortcuts import render, render
from clientes.forms import Crear_cliente, Propiedad, Cartera
from clientes.models import Cliente


# Create your views here.

def clientes_inicio(request):
    return render(request,'clientes/inicio.html',{})

def clientes(request):
    if request.method =='POST':
        formulario=Crear_cliente(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
                    
            nombre_cliente=info_limpia.get('nombre_cliente')
            nombre_popriedad=info_limpia.get('nombre_popriedad')
            num_inmuebles=info_limpia.get('num_inmuebles')
            años_antiguedad=info_limpia.get('años_antiguedad')
            saldo_cartera=info_limpia.get('saldo_cartera')

            cliente = Cliente(
                nombre_cliente=nombre_cliente,
                nombre_popriedad=nombre_popriedad,
                num_inmuebles=num_inmuebles,
                años_antiguedad=años_antiguedad,
                saldo_cartera=saldo_cartera
                )
            
            cliente.save()
            return render(request,'clientes/clientes.html',{'formulario':formulario})
        else:
            return render(request,'clientes/clientes.html',{'formulario':formulario})
    formulario=Crear_cliente()
    return render(request,'clientes/clientes.html',{'formulario':formulario})
    # return render(request,'clientes/clientes.html',{})

def propiedades(request):
    return render(request,'clientes/propiedades.html',{})

def cartera(request):
    return render(request,'clientes/cartera.html',{})
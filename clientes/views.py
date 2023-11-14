from django.shortcuts import render, render, redirect
from clientes.forms import Crear_cliente, Crear_propiedad, Crear_cartera,Buscar_cliente
from clientes.models import Cliente,Propiedad,Cartera


# Create your views here.
def clientes_inicio(request):
    return render(request,'clientes/inicio.html',{})

def clientes(request):
    if request.method =='POST':
        formulario=Crear_cliente(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            num_doc=info_limpia.get('num_doc')
            nombre_cliente=info_limpia.get('nombre_cliente').lower()
            nombre_popriedad=info_limpia.get('nombre_popriedad').lower()
            num_inmuebles=info_limpia.get('num_inmuebles')
            anios_antiguedad=info_limpia.get('anios_antiguedad')
            saldo_cartera=info_limpia.get('saldo_cartera')

            cliente = Cliente(
                num_doc=num_doc,
                nombre_cliente=nombre_cliente,
                nombre_popriedad=nombre_popriedad,
                num_inmuebles=num_inmuebles,
                anios_antiguedad=anios_antiguedad,
                saldo_cartera=saldo_cartera
                )
            
            cliente.save()
            return redirect('/verificacion/Cliente')
        else:
            return render(request,'clientes/clientes.html',{'formulario':formulario})
    formulario=Crear_cliente()
    return render(request,'clientes/clientes.html',{'formulario':formulario})

def propiedades(request):
    if request.method =='POST':
        formulario=Crear_propiedad(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
                    
            tipo=info_limpia.get('tipo')
            descripcion=info_limpia.get('descripcion')
            num_habitaciones=info_limpia.get('num_habitaciones')
            area_total_m2=info_limpia.get('area_total_m2')
            
            propiedad = Propiedad(
                tipo=tipo,
                descripcion=descripcion,
                num_habitaciones=num_habitaciones,
                area_total_m2=area_total_m2
                )
            
            propiedad.save()
            return redirect('/verificacion/Propiedad')
        else:
            return render(request,'clientes/propiedades.html',{'formulario':formulario})
    formulario=Crear_propiedad()
    return render(request,'clientes/propiedades.html',{'formulario':formulario})


def cartera(request):
    if request.method =='POST':
        formulario=Crear_cartera(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
                    
            cliente=info_limpia.get('cliente')
            estado=info_limpia.get('estado')
            saldo=info_limpia.get('saldo')
            dias_mora=info_limpia.get('dias_mora')
            
            cartera = Cartera(
                cliente=cliente,
                estado=estado,
                saldo=saldo,
                dias_mora=dias_mora
                )
            
            cartera.save()
            return redirect('/verificacion/Cartera')
        else:
            return render(request,'clientes/cartera.html',{'formulario':formulario})
    formulario=Crear_cartera()
    return render(request,'clientes/cartera.html',{'formulario':formulario})


def buscar(request):
    cliente_buscar=request.GET.get('Cliente')
    print(request.GET)
    if cliente_buscar:
        lista_clientes=Cliente.objects.filter(nombre_cliente__icontains=cliente_buscar)
    else:
        print('no lo esta cogiendo')
        lista_clientes=Cliente.objects.all()
        
    formulario=Buscar_cliente()
    return render(request,'clientes/buscar.html',{'lista_clientes':lista_clientes,'formulario':formulario})

def verificacion(request,modelo):
    return render(request,'clientes/verificacion.html',{'modelo':modelo})
from django.urls import path, include
from clientes.views import clientes_inicio, clientes, propiedades, cartera

urlpatterns = [
    path('',clientes_inicio),
    path('clientes/',clientes),
    path('propiedades/',propiedades),
    path('cartera/',cartera)
]

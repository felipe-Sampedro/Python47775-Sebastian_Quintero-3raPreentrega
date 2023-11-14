from django.urls import path, include
from clientes.views import clientes_inicio 

urlpatterns = [
    path('',clientes_inicio)
]

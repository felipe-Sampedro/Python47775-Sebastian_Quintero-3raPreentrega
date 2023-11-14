from django.contrib import admin
from clientes.models import Cliente,Propiedad,Cartera

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Propiedad)
admin.site.register(Cartera)
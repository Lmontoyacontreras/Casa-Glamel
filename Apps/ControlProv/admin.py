from django.contrib import admin

from .models import Factura_Provedor,Pedido,Estado

admin.site.register(Factura_Provedor)
admin.site.register(Pedido)
admin.site.register(Estado)

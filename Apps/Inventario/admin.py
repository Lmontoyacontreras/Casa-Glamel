from django.contrib import admin

from .models import Familia,Tipo,Estado,Estado_Ropa,Categoria,Articulo,Color,Talla
# Register your models here.

admin.site.register(Familia)
admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Estado)
admin.site.register(Estado_Ropa)
admin.site.register(Color)
admin.site.register(Talla)

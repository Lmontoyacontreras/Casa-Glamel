from django.conf.urls import url

from .views import Proveedor_Ingresar,Proveedor_Lista,Proveedor_Modificar,Proveedor_Eliminar

urlpatterns = [
    url(r'^Proveedor-Ingresar/$', Proveedor_Ingresar.as_view(), name='Proveedor_Ingresar'),
    url(r'^Proveedor-Lista/$', Proveedor_Lista.as_view(), name='Proveedor_Lista'),
    url(r'^Proveedor-Modificar/(?P<pk>[0-9]+)/$', Proveedor_Modificar.as_view(), name='Proveedor_Modificar'),
    url(r'^Proveedor-Eliminar/(?P<pk>[0-9]+)/$', Proveedor_Eliminar.as_view(), name='Proveedor_Eliminar'),
]


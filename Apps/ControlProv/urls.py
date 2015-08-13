from django.conf.urls import url

from .views import Factura_Proveedor_Ingresar,Pedido_Ingresar,Factura_Proveedor_Lista,Factura_Proveedor_Detail
from .views import Factura_Proveedor_Detail_Imprimir
from .views import Pedido_Eliminar,Factura_Eliminar,Factura_Modificar

urlpatterns = [
    url(r'^Registro-Pedido/$', Factura_Proveedor_Ingresar.as_view(), name='Factura_Proveedor_Ingresar'),
    url(r'^Registro-Pedido/(?P<pk>[0-9]+)/$', Pedido_Ingresar.as_view(), name='Pedido_Ingresar'),
    url(r'^Factura-Proveedor-Lista/$', Factura_Proveedor_Lista.as_view(), name='Factura_Proveedor_Lista'),
    url(r'^Factura-Proveedor-Detail/(?P<pk>[0-9]+)/$', Factura_Proveedor_Detail.as_view(), name='Factura_Proveedor_Detail'),
    url(r'^Factura-Proveedor-Detail-Imprimir/(?P<pk>[0-9]+)/$', Factura_Proveedor_Detail_Imprimir.as_view(), name='Factura_Proveedor_Detail_Imprimir'),

    url(r'^Pedido-Eliminar/(?P<pk>[0-9]+)/$', Pedido_Eliminar.as_view(), name='Pedido_Eliminar'),
    url(r'^Factura-Eliminar/(?P<pk>[0-9]+)/$', Factura_Eliminar.as_view(), name='Factura_Eliminar'),
    url(r'^Factura-Modificar/(?P<pk>[0-9]+)/$', Factura_Modificar.as_view(), name='Factura_Modificar'),
]
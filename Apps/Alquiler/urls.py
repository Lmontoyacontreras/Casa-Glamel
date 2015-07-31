from django.conf.urls import url

from .views import Alquiler_Ingresar,Alquiler_Detail_Ingresar,Alquiler_Factura,Alquiler_Detail_Eliminar,Alquiler_Factura_Imprimir
from .views import Alquiler_Devolucion

urlpatterns = [
    url(r'Alquiler-Ingresar/$', Alquiler_Ingresar.as_view(), name='Alquiler_Ingresar'),
    url(r'Alquiler-Detail-Ingresar/(?P<pk>[0-9]+)/$', Alquiler_Detail_Ingresar.as_view(), name='Alquiler_Detail_Ingresar'),
    url(r'Alquiler-Detail-Eliminar/(?P<pk>[0-9]+)/$', Alquiler_Detail_Eliminar.as_view(), name='Alquiler_Detail_Eliminar'),
    url(r'Alquiler-Factura/(?P<pk>[0-9]+)/$', Alquiler_Factura.as_view(), name='Alquiler_Factura'),
    url(r'Alquiler-Factura-Imprimir/(?P<pk>[0-9]+)/$', Alquiler_Factura_Imprimir.as_view(), name='Alquiler_Factura_Imprimir'),
    url(r'Alquiler-Devolucion/$', Alquiler_Devolucion.as_view(), name='Alquiler_Devolucion'),
]

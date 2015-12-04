from django.conf.urls import url

from .views import IngresarReserva,Reserva_Detail_Ingresar,Reserva_Factura_Detail,Reserva_Factura_Detail_Imprimir,Reserva_Abono
from .views import Reserva_Calendar,Reserva_Detail_Eliminar,Reserva_Devolucion,Reserva_Factura_Detail_Admin,Reserva_List,Reserva_Delete_Admin

urlpatterns = [
    url(r'Reserva-Producto/$',IngresarReserva.as_view(), name='Ingresar_Reserva'),
    url(r'Reserva_Devolucion/$',Reserva_Devolucion.as_view(), name='Reserva_Devolucion'),
    url(r'Reserva-Calendar/$',Reserva_Calendar.as_view(), name='Reserva_Calendar'),
    url(r'Reserva_List/$',Reserva_List.as_view(), name='Reserva_List'),
    url(r'Reserva-Detail-Ingresar/(?P<pk>[0-9]+)/$', Reserva_Detail_Ingresar.as_view(), name='Reserva_Detail_Ingresar'),
    url(r'Reserva-Factura-Detail/(?P<pk>[0-9]+)/$', Reserva_Factura_Detail.as_view(), name='Reserva_Factura_Detail'),
    url(r'Reserva-Factura-Detail-Admin/(?P<pk>[0-9]+)/$', Reserva_Factura_Detail_Admin.as_view(), name='Reserva_Factura_Detail_Admin'),
    url(r'Reserva-Factura-Imprimir/(?P<pk>[0-9]+)/$', Reserva_Factura_Detail_Imprimir.as_view(), name='Reserva_Factura_Detail_Imprimir'),
    url(r'Reserva-Detail-Eliminar/(?P<pk>[0-9]+)/$', Reserva_Detail_Eliminar.as_view(), name='Reserva_Detail_Eliminar'),
    url(r'Reserva-Eliminar/(?P<pk>[0-9]+)/$', Reserva_Delete_Admin.as_view(), name='Reserva_Delete_Admin'),
    url(r'Reserva-Abono/(?P<pk>[0-9]+)/$',Reserva_Abono.as_view(), name='Reserva_Abono'),
]

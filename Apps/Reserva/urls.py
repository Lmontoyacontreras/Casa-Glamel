__author__ = 'Usuario'
from django.conf.urls import url

from .views import IngresarReserva

urlpatterns = [
    url(r'Reserva-Producto/$',IngresarReserva.as_view(), name='Ingresar_Reserva'),
]

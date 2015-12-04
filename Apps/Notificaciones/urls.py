from django.conf.urls import url
from .views import Notificaciones_Ingresar,Notificaciones_List,Notificaciones_Modificar,Notificaciones_Delete


urlpatterns = [
    url(r'^Notificaciones-Ingresar/$', Notificaciones_Ingresar.as_view(), name='Notificaciones_Ingresar'),
    url(r'^Notificaciones-List/$', Notificaciones_List.as_view(), name='Notificaciones_List'),
    url(r'^Notificaciones-Modificar/(?P<pk>[0-9]+)/$', Notificaciones_Modificar.as_view(), name='Notificaciones_Modificar'),
    url(r'^Notificaciones-Delete/(?P<pk>[0-9]+)/$', Notificaciones_Delete.as_view(), name='Notificaciones_Delete'),
]
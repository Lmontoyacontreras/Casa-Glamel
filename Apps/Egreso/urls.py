from django.conf.urls import url
from .views import Egreso_Ingresar,Egreso_Delete,Egreso_Modificar,Egreso_List

urlpatterns = [
    url(r'^Egreso-Ingresar/$', Egreso_Ingresar.as_view(), name='Egreso_Ingresar'),
    url(r'^Egreso-List/$', Egreso_List.as_view(), name='Egreso_List'),
    url(r'^Egreso-Modificar/(?P<pk>[0-9]+)/$', Egreso_Modificar.as_view(), name='Egreso_Modificar'),
    url(r'^Egreso-Delete/(?P<pk>[0-9]+)/$', Egreso_Delete.as_view(), name='Egreso_Delete'),
]
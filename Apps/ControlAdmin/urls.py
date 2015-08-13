from django.conf.urls import url

from .views import Seguimiento_Prendas,Seguimiento_Detail

urlpatterns = [
    url(r'Seguimiento-Prendas/$', Seguimiento_Prendas.as_view(), name='Seguimiento_Prendas'),
    url(r'Seguimiento_Detail/(?P<pk>[0-9]+)/$', Seguimiento_Detail.as_view(), name='Seguimiento_Detail'),
]

from django.conf.urls import url

from .views import Home_Admin,Ventas_Control

urlpatterns = [
    url(r'Home-Admin/$', Home_Admin.as_view(), name='Home_Admin'),
    url(r'Ventas-Control/$', Ventas_Control, name='Ventas_Control'),
]

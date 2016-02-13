__author__ = 'Usuario'
# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import Familia_Ingresar,Familia_Lista,Familia_Modificar,Familia_Eliminar
from .views import Categoria_Ingresar, Categoria_Lista, Categoria_Modificar,Categoria_Eliminar
from .views import Articulo_Ingresar,Articulo_Modificar, Articulo_Lista, Articulo_Detail,Articulo_Eliminar
from .views import Inventario_Lista

urlpatterns = [
    url(r'^Familia-Ingresar/$', Familia_Ingresar.as_view(), name='Familia_Ingresar'),
    url(r'^Familia-Lista/$', Familia_Lista.as_view(), name='Familia_Lista'),
    url(r'^Familia-Modificar/(?P<pk>[0-9]+)/$', Familia_Modificar.as_view(), name='Familia_Modificar'),
    url(r'^Familia-Eliminar/(?P<pk>[0-9]+)/$', Familia_Eliminar.as_view(), name='Familia_Eliminar'),

    url(r'^Categoria-Ingresar/$', Categoria_Ingresar.as_view(), name='Categoria_Ingresar'),
    url(r'^Categoria-Lista/$', Categoria_Lista.as_view(), name='Categoria_Lista'),
    url(r'^Categoria-Modificar/(?P<pk>[0-9]+)/$', Categoria_Modificar.as_view(), name='Categoria_Modificar'),
    url(r'^Categoria-Eliminar/(?P<pk>[0-9]+)/$', Categoria_Eliminar.as_view(), name='Categoria_Eliminar'),

    url(r'^Articulo-Ingresar/$', Articulo_Ingresar.as_view(), name='Articulo_Ingresar'),
    url(r'^Articulo-Modificar/(?P<pk>[0-9]+)/$', Articulo_Modificar.as_view(), name='Articulo_Modificar'),
    url(r'^Articulo-Lista/$', Articulo_Lista.as_view(), name='Ariculo_Lista'),
    url(r'^Articulo-Detail/(?P<pk>[0-9]+)/$', Articulo_Detail.as_view(), name='Articulo_Detail'),
    url(r'^Articulo-Eliminar/(?P<pk>[0-9]+)/$', Articulo_Eliminar.as_view(), name='Articulo_Eliminar'),

    url(r'^objects/page(?P<page>[0-9]+)/$', Articulo_Lista.as_view()),

    url(r'^Inventario-Lista/$', Inventario_Lista.as_view(), name='Inventario_Lista'),
    url(r'^objects/page(?P<page>[0-9]+)/$', Inventario_Lista.as_view()),


]

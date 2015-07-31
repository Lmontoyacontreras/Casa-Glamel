from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

from .forms import Proveedor_Form
from .models import Proveedor

class Proveedor_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    model = Proveedor
    login_url = '/'
    template_name = u'ModuloAdmin/GestionTemplate/Proveedor/proveedor_form.html'
    form_class = Proveedor_Form
    success_url = reverse_lazy('Gestion:Proveedor_Lista')

class Proveedor_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Proveedor
    login_url = '/'
    context_object_name = 'proveedor'
    template_name = u'ModuloAdmin/GestionTemplate/Proveedor/proveedor_list.html'

class Proveedor_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Proveedor
    login_url = '/'
    template_name = u'ModuloAdmin/GestionTemplate/Proveedor/proveedor_form.html'
    form_class = Proveedor_Form
    success_url = reverse_lazy('Gestion:Proveedor_Lista')

class Proveedor_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Proveedor
    login_url = '/'
    template_name = u'ModuloAdmin/GestionTemplate/Proveedor/proveedor_confirm_delete.html'
    context_object_name = 'proveedor'
    success_url = reverse_lazy('Gestion:Proveedor_Lista')



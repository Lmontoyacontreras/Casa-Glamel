from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin

from .models import Familia, Categoria, Articulo
from .forms import Familia_Form, Categoria_Form, Articulo_Form

#LoginRequiredMixin,

class Familia_Ingresar(LoginRequiredMixin,CreateView):
    model = Familia
    login_url = '/'
    template_name = 'ModuloAdmin/InventarioTemplate/Familia/familia_form.html'
    form_class = Familia_Form
    success_url = reverse_lazy('Inventario:Familia_Lista')


class Familia_Lista(LoginRequiredMixin,ListView):
    model = Familia
    login_url = '/'
    template_name = 'ModuloAdmin/InventarioTemplate/Familia/familia_list.html'
    context_object_name = 'familia'


class Familia_Modificar(LoginRequiredMixin,UpdateView):
    model = Familia
    login_url = '/'
    template_name = 'ModuloAdmin/InventarioTemplate/Familia/familia_form.html'
    form_class = Familia_Form
    success_url = reverse_lazy('Inventario:Familia_Lista')


class Familia_Eliminar(LoginRequiredMixin,DeleteView):
    model = Familia
    login_url = '/'
    context_object_name = 'familia'
    template_name = 'ModuloAdmin/InventarioTemplate/Familia/familia_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Familia_Lista')

# Categoria

class Categoria_Ingresar(LoginRequiredMixin,CreateView):
    model = Categoria
    login_url = '/'
    form_class = Categoria_Form
    template_name = 'ModuloAdmin/InventarioTemplate/Categoria/categoria_form.html'
    success_url = reverse_lazy('Inventario:Categoria_Lista')

class Categoria_Lista(LoginRequiredMixin,ListView):
    model = Categoria
    login_url = '/'
    context_object_name = 'categoria'
    template_name = 'ModuloAdmin/InventarioTemplate/Categoria/categoria_list.html'

class Categoria_Modificar(LoginRequiredMixin,UpdateView):
    model = Categoria
    login_url = '/'
    template_name = 'ModuloAdmin/InventarioTemplate/Categoria/categoria_form.html'
    form_class = Categoria_Form
    success_url = reverse_lazy('Inventario:Categoria_Lista')

class Categoria_Eliminar(LoginRequiredMixin,DeleteView):
    model = Categoria
    login_url = '/'
    context_object_name = 'categoria'
    template_name = 'ModuloAdmin/InventarioTemplate/Categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Categoria_Lista')

#Articulos

class Articulo_Ingresar(LoginRequiredMixin,CreateView):
    model = Articulo
    login_url = '/'
    form_class = Articulo_Form
    template_name = 'ModuloAdmin/InventarioTemplate/Articulo/articulo_form.html'
    success_url = reverse_lazy('Inventario:Ariculo_Lista')

class Articulo_Lista(LoginRequiredMixin,ListView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = 'ModuloAdmin/InventarioTemplate/Articulo/articulo_list.html'

class Articulo_Detail(LoginRequiredMixin,DetailView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = 'ModuloAdmin/InventarioTemplate/Articulo/articulo_detail.html'

class Articulo_Modificar(LoginRequiredMixin,UpdateView):
    model = Articulo
    login_url = '/'
    template_name = 'ModuloAdmin/InventarioTemplate/Articulo/articulo_form.html'
    form_class = Articulo_Form
    success_url = reverse_lazy('Inventario:Ariculo_Lista')

class Articulo_Eliminar(LoginRequiredMixin,DeleteView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = 'ModuloAdmin/InventarioTemplate/Articulo/articulo_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Ariculo_Lista')

class Inventario_Lista(LoginRequiredMixin,ListView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = 'ModuloAdmin/InventarioTemplate/Inventario/Inventario_List.html'

    def get_context_data(self, **kwargs):
        context = super(Inventario_Lista,self).get_context_data(**kwargs)
        context['articulo_disponible'] = Articulo.objects.filter(nombre_estado='1', nombre_estado_ropa=1)
        context['articulo_alquilado'] = Articulo.objects.filter(nombre_estado='2',nombre_estado_ropa=1)
        context['articulo_danado'] = Articulo.objects.filter(nombre_estado_ropa='2')
        return context
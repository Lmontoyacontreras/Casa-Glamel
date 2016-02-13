from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

from .models import Familia, Categoria, Articulo
from .forms import Familia_Form, Categoria_Form, Articulo_Form

#LoginRequiredMixin,
class Familia_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    model = Familia
    login_url = '/'
    template_name = u'ModuloAdmin/InventarioTemplate/Familia/familia_form.html'
    form_class = Familia_Form
    success_url = reverse_lazy('Inventario:Familia_Lista')


class Familia_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Familia
    login_url = '/'
    template_name = u'ModuloAdmin/InventarioTemplate/Familia/familia_list.html'
    context_object_name = 'familia'


class Familia_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Familia
    login_url = '/'
    template_name = u'ModuloAdmin/InventarioTemplate/Familia/familia_form.html'
    form_class = Familia_Form
    success_url = reverse_lazy('Inventario:Familia_Lista')


class Familia_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Familia
    login_url = '/'
    context_object_name = 'familia'
    template_name = u'ModuloAdmin/InventarioTemplate/Familia/familia_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Familia_Lista')

# Categoria

class Categoria_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    model = Categoria
    login_url = '/'
    form_class = Categoria_Form
    template_name = u'ModuloAdmin/InventarioTemplate/Categoria/categoria_form.html'
    success_url = reverse_lazy('Inventario:Categoria_Lista')

class Categoria_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Categoria
    login_url = '/'
    context_object_name = 'categoria'
    template_name = u'ModuloAdmin/InventarioTemplate/Categoria/categoria_list.html'

class Categoria_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Categoria
    login_url = '/'
    template_name = u'ModuloAdmin/InventarioTemplate/Categoria/categoria_form.html'
    form_class = Categoria_Form
    success_url = reverse_lazy('Inventario:Categoria_Lista')

class Categoria_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Categoria
    login_url = '/'
    context_object_name = 'categoria'
    template_name = u'ModuloAdmin/InventarioTemplate/Categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Categoria_Lista')

#Articulos

class Articulo_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    model = Articulo
    login_url = '/'
    form_class = Articulo_Form
    template_name = u'ModuloAdmin/InventarioTemplate/Articulo/articulo_form.html'
    success_url = reverse_lazy('Inventario:Ariculo_Lista')

class Articulo_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = u'ModuloAdmin/InventarioTemplate/Articulo/articulo_list.html'
    paginate_by = 10

class Articulo_Detail(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = u'ModuloAdmin/InventarioTemplate/Articulo/articulo_detail.html'

class Articulo_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Articulo
    login_url = '/'
    template_name = u'ModuloAdmin/InventarioTemplate/Articulo/articulo_form.html'
    form_class = Articulo_Form
    success_url = reverse_lazy('Inventario:Ariculo_Lista')

class Articulo_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Articulo
    login_url = '/'
    context_object_name = 'articulo'
    template_name = u'ModuloAdmin/InventarioTemplate/Articulo/articulo_confirm_delete.html'
    success_url = reverse_lazy('Inventario:Articulo_Ingresar')

class Inventario_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    queryset = Articulo.objects.filter(nombre_estado=1, nombre_estado_ropa=1)
    login_url = '/'
    context_object_name = 'articulo_disponible'
    template_name = u'ModuloAdmin/InventarioTemplate/Inventario/Inventario_List.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Inventario_Lista,self).get_context_data(**kwargs)
        context['articulo_alquilado'] = Articulo.objects.filter(nombre_estado=1,nombre_estado_ropa=2)
        context['articulo_danado'] = Articulo.objects.filter(nombre_estado='2')
        return context
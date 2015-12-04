from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic import ListView
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import Notificaciones
from .forms import Notificaciones_Form

class Notificaciones_Ingresar(LoginRequiredMixin,CreateView):
    model = Notificaciones
    login_url = '/'
    template_name = 'ModuloRecepcionista/Otros/Notificaciones/notificaciones_form.html'
    form_class = Notificaciones_Form
    success_url = reverse_lazy('Notificaciones:Notificaciones_Ingresar')



class Notificaciones_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Notificaciones
    login_url = '/'
    template_name = u'ModuloAdmin/Otros/Notificaciones/notificaciones_form.html'
    form_class = Notificaciones_Form
    success_url = reverse_lazy('Notificaciones:Notificaciones_List')


class Notificaciones_List(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Notificaciones
    login_url = '/'
    template_name = u'ModuloAdmin/Otros/Notificaciones/notificaciones_list.html'
    context_object_name = 'notificaciones'


class Notificaciones_Delete(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Notificaciones
    login_url = '/'
    context_object_name = 'notificaciones'
    template_name = u'ModuloAdmin/Otros/Notificaciones/notificaciones_comfirm_delete.html'
    success_url = reverse_lazy('Notificaciones:Notificaciones_List')
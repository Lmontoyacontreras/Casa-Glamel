from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin
from django.core.urlresolvers import reverse_lazy


from .models import Egreso
from .forms import Egreso_Form

class Egreso_Ingresar(LoginRequiredMixin,CreateView):
    model = Egreso
    template_name = 'ModuloRecepcionista/Otros/Egresos/egreso_form.html'
    form_class = Egreso_Form
    login_url = '/'
    success_url = reverse_lazy('Egreso:Egreso_Ingresar')


class Egreso_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = Egreso
    login_url = '/'
    template_name = u'ModuloAdmin/Otros/Egresos/egresos_form.html'
    form_class = Egreso_Form
    success_url = reverse_lazy('Egreso:Egreso_List')


class Egreso_List(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Egreso
    login_url = '/'
    template_name = u'ModuloAdmin/Otros/Egresos/egresos_list.html'
    context_object_name = 'egreso'


class Egreso_Delete(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Egreso
    login_url = '/'
    context_object_name = 'egreso'
    template_name = u'ModuloAdmin/Otros/Egresos/egresos_comfirm_delete.html'
    success_url = reverse_lazy('Egreso:Egreso_List')
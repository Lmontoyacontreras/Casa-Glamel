from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Reserva
from .forms import Reserva_Form

# Create your views here.
class IngresarReserva(CreateView):
    model = Reserva
    form_class = Reserva_Form
    template_name = 'ModuloRecepcionista/Reserva/Reserva_form.html'
    success_url = reverse_lazy('Alquiler:Alquiler_Ingresar')
    def form_valid(self, form):
        user = self.request.user
        form.instance.vendedor = user
        return super(IngresarReserva,self).form_valid(form)


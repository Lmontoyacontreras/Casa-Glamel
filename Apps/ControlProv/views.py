from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin

from .forms import Factura_Provedor_Form,Pedido_Form
from .models import Factura_Provedor,Pedido
from Apps.GestionInf.models import Proveedor

class Factura_Proveedor_Ingresar(LoginRequiredMixin,CreateView):
    model = Factura_Provedor
    login_url = '/'
    template_name = 'ModuloAdmin/ControlTemplate/factura_proveedor_form.html'
    form_class = Factura_Provedor_Form


class Pedido_Ingresar(LoginRequiredMixin,DetailView):
    model = Factura_Provedor
    login_url = '/'
    template_name = 'ModuloAdmin/ControlTemplate/pedido_form.html'
    context_object_name = 'factura_proveedor'

    def get_context_data(self, **kwargs):
        context = super(Pedido_Ingresar,self).get_context_data(**kwargs)
        context['pedido_detalle'] = Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        context['form'] = Pedido_Form()
        return context

    def post(self,request,*args,**kwargs):
        form = Pedido_Form(request.POST.copy())
        form.instance.factura_Proveedor = self.get_object()
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ControlProv:Pedido_Ingresar', args=[self.get_object().pk]))


class Factura_Proveedor_Lista(LoginRequiredMixin,ListView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura'
    template_name = 'ModuloAdmin/ControlTemplate/factura_proveedor_list.html'


class Factura_Proveedor_Detail(LoginRequiredMixin,DetailView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura_proveedor'
    template_name = 'ModuloAdmin/ControlTemplate/factura_proveedor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Factura_Proveedor_Detail,self).get_context_data(**kwargs)
        context['pedido_detalle']= Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        context['pedido_proveedor']= Proveedor.objects.filter(nombre_Empresa=self.get_object().nombre_Empresa)
        proveedor_cuentas = Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        cuentas = []
        suma = 0
        for i in proveedor_cuentas:
            cuentas.append(i.cantidad * i.precio)
            suma = suma + (i.cantidad * i.precio)
        context['cuentas']=cuentas
        context['suma']=suma
        return context


class Factura_Proveedor_Detail_Imprimir(LoginRequiredMixin,DetailView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura_proveedor'
    template_name = 'ModuloAdmin/ControlTemplate/factura_proveedor_detail_imprimir.html'

    def get_context_data(self, **kwargs):
        context = super(Factura_Proveedor_Detail_Imprimir,self).get_context_data(**kwargs)
        context['pedido_detalle']= Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        context['pedido_proveedor']= Proveedor.objects.filter(nombre_Empresa=self.get_object().nombre_Empresa)
        proveedor_cuentas = Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        cuentas = []
        suma = 0
        for i in proveedor_cuentas:
            cuentas.append(i.cantidad * i.precio)
            suma = suma + (i.cantidad * i.precio)
        context['cuentas']=cuentas
        context['suma']=suma
        return context
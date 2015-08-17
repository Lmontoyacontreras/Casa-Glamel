from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

from .forms import Factura_Provedor_Form,Pedido_Form
from .models import Factura_Provedor,Pedido
from Apps.GestionInf.models import Proveedor

class Factura_Proveedor_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,CreateView):
    model = Factura_Provedor
    login_url = '/'
    template_name = u'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_form.html'
    form_class = Factura_Provedor_Form


class Pedido_Ingresar(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    model = Factura_Provedor
    login_url = '/'
    template_name = u'ModuloAdmin/ControlTemplate/PedidoTemplate/pedido_form.html'
    context_object_name = 'factura_proveedor'

    def get_context_data(self, **kwargs):
        context = super(Pedido_Ingresar,self).get_context_data(**kwargs)
        context['pedido_detalle'] = Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        context['form'] = Pedido_Form()
        return context

    def post(self,request,*args,**kwargs):
        form = Pedido_Form(request.POST.copy())
        form.instance.factura_Proveedor = self.get_object()
        valor= int(form.data['cantidad'])*int(form.data['precio'])
        form.instance.precio_total = valor
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('ControlProv:Pedido_Ingresar', args=[self.get_object().pk]))


class Factura_Proveedor_Lista(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura'
    template_name = u'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_list.html'


class Factura_Proveedor_Detail(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura_proveedor'
    template_name = u'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Factura_Proveedor_Detail,self).get_context_data(**kwargs)
        context['pedido_detalle']= Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        context['pedido_proveedor']= Proveedor.objects.filter(nombre_Empresa=self.get_object().nombre_Empresa)
        proveedor_cuentas = Pedido.objects.filter(factura_Proveedor=self.get_object().pk)
        suma = 0
        for i in proveedor_cuentas:
            suma = suma + (i.cantidad * i.precio)
        context['suma']=suma
        return context


class Factura_Proveedor_Detail_Imprimir(Factura_Proveedor_Detail):
    template_name = 'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_detail_imprimir.html'


class Pedido_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    context_object_name = 'pedido'
    model = Pedido
    template_name = 'ModuloAdmin/ControlTemplate/PedidoTemplate/pedido_confirm_delete.html'

    def post(self,request,*args,**kwargs):
        factura_pedido_detail = self.get_object()
        pedido_detail = self.get_object().factura_Proveedor
        factura_pedido_detail.delete()
        return HttpResponseRedirect(reverse('ControlProv:Pedido_Ingresar', args=[pedido_detail]))


class Factura_Eliminar(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Factura_Provedor
    login_url = '/'
    context_object_name = 'factura_proveedor'
    template_name = u'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_confirm_delete.html'
    success_url = reverse_lazy('ControlProv:Factura_Proveedor_Lista')

class Factura_Modificar(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    template_name = u'ModuloAdmin/ControlTemplate/FacturaTemaplete/factura_proveedor_form.html'
    login_url = '/'
    form_class = Factura_Provedor_Form
    model = Factura_Provedor
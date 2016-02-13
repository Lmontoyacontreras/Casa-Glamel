from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView,ListView,TemplateView
from datetime import date,timedelta
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin


from .models import Reserva,Reserva_Detail
from .forms import Reserva_Form,Reserva_Detail_Form,Reserva_Form_Abono
from Apps.Inventario.models import Articulo,Estado_Ropa
from Apps.Alquiler.models import Alquiler,Alquiler_Detail
from Apps.Alquiler.forms import Alquiler_Reserva_Form
from Apps.GestionInf.models import Cliente

# Create your views here.
class IngresarReserva(LoginRequiredMixin,CreateView):
    model = Reserva
    login_url = '/'
    form_class = Reserva_Form
    template_name = 'ModuloRecepcionista/Reserva/Reserva_form.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.vendedor = user
        cliente = Cliente.objects.get(pk=form.instance.cliente.pk)
        cliente.numeros_compras += 1
        cliente.save()
        return super(IngresarReserva,self).form_valid(form)

class Reserva_Abono(LoginRequiredMixin,UpdateView):
    model = Reserva
    login_url = '/'
    form_class = Reserva_Form_Abono
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Abono.html'


class Reserva_Detail_Ingresar(LoginRequiredMixin,DetailView):
    model = Reserva
    login_url = '/'
    context_object_name = 'reserva'
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(Reserva_Detail_Ingresar,self).get_context_data(**kwargs)
        definicion_cortesia = False
        cliente = Cliente.objects.get(pk=self.get_object().cliente.pk)
        if cliente.numeros_compras%10==0:
            definicion_cortesia = True
        context['cortesia'] = definicion_cortesia
        context['reserva_detail']=Reserva_Detail.objects.filter(reserva=self.get_object())
        Reserva_Detail_Filtro = Reserva_Detail_Form()
        dia_max=self.get_object().fecha_reserva-timedelta(days=6)
        dia_min=self.get_object().fecha_limite
        reserva_view = Reserva.objects.filter(fecha_reserva__range=(dia_max,dia_min))
        lista_articulo = []
        for res in reserva_view:
            reserva_detail_view = Reserva_Detail.objects.filter(reserva=res.pk)
            for reserva_detail_view in reserva_detail_view:
                articulo = Articulo.objects.get(referencia=reserva_detail_view.articulo)
                lista_articulo.append(articulo.pk)
        ac = Articulo.objects.exclude(pk__in=lista_articulo)
        Reserva_Detail_Filtro.fields['articulo'].queryset = ac.filter(nombre_estado_ropa=1)
        context['form']=Reserva_Detail_Filtro
        return context

    def post(self,request,*args,**kwargs):
        form = Reserva_Detail_Form(request.POST.copy())
        form.instance.reserva = self.get_object()
        gratis = request.POST.get('gratis',False)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('Reservas:Reserva_Detail_Ingresar', args=[self.get_object().pk]))


class Reserva_Factura_Detail(LoginRequiredMixin,DetailView):
    model = Reserva
    login_url = '/'
    context_object_name = 'reserva'
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Factura_Detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(Reserva_Factura_Detail,self).get_context_data(**kwargs)
        context['reserva_detail_factura'] = Reserva_Detail.objects.filter(reserva=self.get_object())
        deta = Reserva_Detail.objects.filter(reserva=self.get_object())
        suma = 0
        for deta in deta:
            if deta.gratis:
                suma += 0
            else:
                suma += deta.articulo.precio
        suma = suma-(suma*self.get_object().descuento/100)
        context['hoy']=date.today()
        context['form']=Alquiler_Reserva_Form()
        context['suma']=suma
        context['total']=suma-self.get_object().abono_inicial
        return context

    def post(self,request,*args,**kwargs):
        user = self.request.user
        form = Alquiler_Reserva_Form(request.POST.copy())
        form.data['vendedor'] = self.get_object().vendedor
        cliente = Cliente.objects.get(full_nombre=self.get_object().cliente)
        form.data['cliente'] = cliente.pk
        form.data['descuento'] = self.get_object().descuento
        hoy = date.today()
        form.data['fecha_entrega'] = hoy
        form.instance.devuelto = False
        form.instance.fecha_devolucion_dia = hoy
        form.instance.multa= 0
        if form.is_valid():
            obj = form.save()
            for x in Reserva_Detail.objects.filter(reserva=self.get_object()):
                articulo = Articulo.objects.get(pk=x.articulo.pk)
                cambio_estado = Estado_Ropa.objects.get(pk=2)
                articulo.nombre_estado_ropa = cambio_estado
                articulo.save()
                alquil = Alquiler_Detail()
                alquil.alquiler = obj
                alquil.articulo = x.articulo
                alquil.gratis = x.gratis
                if alquil.gratis:
                    alquil.precio = 0
                else:
                    alquil.precio = x.articulo.precio
                alquil.save()
            a = Reserva.objects.get(pk=self.get_object().pk)
            a.delete()
            if not user.is_staff:
                return HttpResponseRedirect(reverse('Alquiler:Alquiler_Factura', args=[obj.pk]))
            else:
                return HttpResponseRedirect(reverse('Alquiler:Alquiler_Factura_detail', args=[obj.pk]))
        if not user.is_staff:
            return HttpResponseRedirect(reverse('Reservas:Reserva_Factura_Detail',args=[self.get_object().pk]))
        else:
            return HttpResponseRedirect(reverse('Reservas:Reserva_Factura_Detail_Admin', args=[self.get_object().pk]))


class Reserva_Factura_Detail_Imprimir(Reserva_Factura_Detail):
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Factura_Imprimir.html'


class Reserva_Calendar(LoginRequiredMixin,ListView):
    model = Reserva
    login_url = '/'
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Calendar.html'
    context_object_name = 'reserva'

class Reserva_List (SuperuserRequiredMixin,LoginRequiredMixin,ListView):
    model = Reserva
    login_url = '/'
    template_name = u'ModuloAdmin/Reserva/Reserva_List.html'
    context_object_name = 'reserva'


class Reserva_Detail_Eliminar(LoginRequiredMixin,DetailView):
    context_object_name = 'reserva'
    model = Reserva_Detail
    login_url = '/'
    template_name = 'ModuloRecepcionista/Reserva/Reserva_delete_confirm.html'

    def post(self,request,*args,**kwargs):
        reserva_pedido_detail = self.get_object()
        reserva_detail_a = self.get_object().reserva
        reserva_pedido_detail.delete()
        return HttpResponseRedirect(reverse('Reservas:Reserva_Detail_Ingresar', args=[reserva_detail_a]))

class Reserva_Devolucion(LoginRequiredMixin,TemplateView):
    login_url = '/'
    template_name = 'ModuloRecepcionista/Reserva/Reserva_Devolucion.html'

    def post(self,request,*args,**kwargs):
        alquiler_factura = request.POST.get('alquiler_factura')
        if alquiler_factura.isdigit():
            valida = Reserva.objects.filter(pk=alquiler_factura).exists()
            if valida:
                ref = Reserva.objects.get(pk=alquiler_factura)
                return HttpResponseRedirect(reverse('Reservas:Reserva_Factura_Detail', args=[ref.pk]))
        return render(request,'ModuloRecepcionista/Reserva/Reserva_Devolucion.html')


class Reserva_Factura_Detail_Admin(Reserva_Factura_Detail):
    template_name = 'ModuloAdmin/Reserva/Reserva_Factura.html'


class Reserva_Delete_Admin(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = Reserva
    login_url = '/'
    context_object_name = 'reserva'
    template_name = u'ModuloAdmin/Reserva/Reserva_Confirm_Delete.html'
    success_url = reverse_lazy('Reservas:Reserva_List')
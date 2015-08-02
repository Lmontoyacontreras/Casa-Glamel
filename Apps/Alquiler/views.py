from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView
from django.views.generic import TemplateView,DetailView
from django.core.urlresolvers import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from braces.views import LoginRequiredMixin

from .forms import Alquiler_Form,Alquiler_Detail_Form
from .models import Alquiler,Alquiler_Detail
from Apps.Inventario.models import Articulo,Estado_Ropa

class Alquiler_Ingresar(LoginRequiredMixin,CreateView):
    model = Alquiler
    form_class = Alquiler_Form
    login_url = '/'
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDetailTemplate/alquiler_form.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.vendedor = user
        return super(Alquiler_Ingresar,self).form_valid(form)

class Alquiler_Detail_Ingresar(LoginRequiredMixin,DetailView):
    model = Alquiler
    login_url = '/'
    context_object_name = 'alquiler_factura'
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDetailTemplate/alquiler_detail_form.html'

    def get_context_data(self, **kwargs):
        context = super(Alquiler_Detail_Ingresar, self).get_context_data(**kwargs)
        context['alquiler_detalle'] = Alquiler_Detail.objects.filter(alquiler=self.get_object())
        Alquiler_Detail_Filtro = Alquiler_Detail_Form()
        Alquiler_Detail_Filtro.fields["articulo"].queryset = Articulo.objects.filter(nombre_estado_ropa='1',nombre_estado='1')
        context['form'] = Alquiler_Detail_Filtro
        return context

    def post(self,request,*args,**kwargs):
        form = Alquiler_Detail_Form(request.POST.copy())
        form.instance.alquiler = self.get_object()
        articulo = Articulo.objects.get(pk=form.data['articulo'])
        cambio_estado = Estado_Ropa.objects.get(pk=2)
        articulo.nombre_estado_ropa = cambio_estado
        articulo.save()
        gratis = request.POST.get('gratis',False)
        form.data['gratis']=gratis
        if gratis:
            form.data['precio']=0
        else:
            form.data['precio']=articulo.precio
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('Alquiler:Alquiler_Detail_Ingresar', args=[self.get_object().pk]))


class Alquiler_Detail_Eliminar(LoginRequiredMixin,DetailView):
    model = Alquiler_Detail
    login_url = '/'
    context_object_name = 'articulo'
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDetailTemplate/alquiler_confirm_delete.html'

    def post(self,request,*args,**kwargs):
        articulo_detail = self.get_object()
        a = self.get_object().alquiler
        articulo = Articulo.objects.get(pk=articulo_detail.articulo.pk)
        cambio_estado = Estado_Ropa.objects.get(pk=1)
        articulo.nombre_estado_ropa = cambio_estado
        articulo.save()
        articulo_detail.delete()
        return HttpResponseRedirect(reverse('Alquiler:Alquiler_Detail_Ingresar', args=[a]))

class Alquiler_Factura(LoginRequiredMixin,DetailView):
    model = Alquiler
    login_url = '/'
    context_object_name = 'alquiler'
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDetailTemplate/alquiler_factura_form.html'

    def get_context_data(self, **kwargs):
        cotext = super(Alquiler_Factura,self).get_context_data(**kwargs)
        cotext['alquiler_detail'] = Alquiler_Detail.objects.filter(alquiler=self.get_object().pk)
        alquiler_detail_suma = Alquiler_Detail.objects.filter(alquiler=self.get_object().pk)
        suma = 0
        suma_original = 0
        for alquiler in alquiler_detail_suma:
            suma=alquiler.precio+suma
            suma_original=suma_original+alquiler.articulo.precio_original
        cotext['suma'] = suma
        cotext['suma_original'] = suma_original
        return cotext

    def post(self,request,*args,**kwargs):
        alquiler = self.get_object()
        alquiler_detail = Alquiler_Detail.objects.filter(alquiler=self.get_object().pk)
        alquiler.devuelto = True
        cambio_estado = Estado_Ropa.objects.get(pk=3)
        for alquiler_detail in alquiler_detail:
            articulo = Articulo.objects.get(referencia=alquiler_detail.articulo)
            articulo.nombre_estado_ropa=cambio_estado
            articulo.save()
        alquiler.save()
        return render(request,'ModuloRecepcionista/Alquiler/AlquilerDevolucionTemplate/Alquiler_Devolucion.html')


class Alquiler_Factura_Imprimir(Alquiler_Factura):
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDetailTemplate/alquiler_factura_imprimir.html'


class Alquiler_Devolucion(LoginRequiredMixin,TemplateView):
    login_url = '/'
    template_name = 'ModuloRecepcionista/Alquiler/AlquilerDevolucionTemplate/Alquiler_Devolucion.html'

    def post(self,request,*args,**kwargs):
        alquiler_factura = request.POST.get('alquiler_factura')
        valida = Alquiler.objects.filter(pk=alquiler_factura)
        if valida:
            return HttpResponseRedirect(reverse('Alquiler:Alquiler_Factura', args=[alquiler_factura]))
        else:
            return render(request,'ModuloRecepcionista/Alquiler/AlquilerDevolucionTemplate/Alquiler_Devolucion.html',
                          {'valida':valida})
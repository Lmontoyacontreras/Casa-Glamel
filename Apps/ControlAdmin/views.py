from django.shortcuts import render
from django.views.generic import TemplateView,DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy,reverse


# Create your views here.
from Apps.Inventario.models import Articulo
from Apps.Alquiler.models import Alquiler,Alquiler_Detail

class Seguimiento_Prendas(TemplateView):
    template_name = 'ModuloAdmin/AdminControlTemplate/Seguimineto_Prendas.html'

    def post(self,request,*args,**kwargs):
        ref = request.POST.get('seguimiento_articulo')
        valida = Articulo.objects.filter(referencia=ref).exists()
        if valida:
            referencia = Articulo.objects.get(referencia=ref)
            return HttpResponseRedirect(reverse('ControlAdmin:Seguimiento_Detail', args=[referencia.pk]))
        else:
            return render(request,'ModuloAdmin/AdminControlTemplate/Seguimineto_Prendas.html',
                          {'valida':valida})

class Seguimiento_Detail(DetailView):
    model = Articulo
    context_object_name = 'articulo'
    template_name = 'ModuloAdmin/AdminControlTemplate/Seguimiento Detail.html'

    def get_context_data(self, **kwargs):
        context = super(Seguimiento_Detail,self).get_context_data(**kwargs)
        aritculo_detail = Alquiler_Detail.objects.filter(articulo=self.get_object().pk)
        cantidad = aritculo_detail.count()
        context['historial'] = aritculo_detail
        context['cantidad'] = cantidad
        return context
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date,timedelta
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin

from Apps.Egreso.models import Egreso
from Apps.Inventario.models import Categoria,Articulo,Tipo
from Apps.Alquiler.models import Alquiler_Detail,Alquiler
from Apps.Reserva.models import Reserva,Reserva_Detail
from Apps.GestionInf.models import Cliente
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def Ventas_Control(request):
    tmp = 'ModuloAdmin/VentasTemplate/Ventas_Control_Template.html'
    registro = False
    if request.method=='POST':
        fecha_inicio = request.POST.get('Fecha_Inicio')
        fecha_final = request.POST.get('Fecha_Final')
        fecha_ini = date(int(fecha_inicio[6:]),int(fecha_inicio[3:5]),int(fecha_inicio[0:2]))
        fecha_fin = date(int(fecha_final[6:]),int(fecha_final[3:5]),int(fecha_final[0:2]))
        if(fecha_fin>fecha_ini):
            registro = True
            alqui = Alquiler.objects.filter(fecha_entrega__range=(fecha_ini,fecha_fin))
            alqui_suma = 0

            for alqui in alqui:
                alqui_detail = Alquiler_Detail.objects.filter(alquiler=alqui.pk)
                for alqui_detail in alqui_detail:
                    alqui_suma += alqui_detail.precio-(alqui_detail.precio*(alqui.descuento/100))

            multa = Alquiler.objects.filter(fecha_devolucion_dia__range=(fecha_ini,fecha_fin))
            multa_suma = 0
            for multa in multa:
                multa_suma += multa.multa
            rese = Reserva.objects.filter(fecha_limite__lt=fecha_fin, fecha_reserva__gt=fecha_ini)
            reserva_cadu = 0
            for rese in rese:
                reserva_cadu += rese.abono_inicial
            egreso_suma = 0
            egreso = Egreso.objects.filter(fecha__range=(fecha_ini,fecha_fin))
            for egreso in egreso:
                egreso_suma += egreso.valor
            suma_total = multa_suma+alqui_suma+reserva_cadu-egreso_suma


            return render(request,tmp,{'registro':registro,'fecha_inicio':fecha_ini,'fecha_final':fecha_fin,
                                       'alqui_suma':alqui_suma,'multa_suma':multa_suma,'suma_total':suma_total,
                                       'reserva_cadu':reserva_cadu, 'egreso_suma':egreso_suma })
        else:
            return render(request,tmp,{'registro':registro})
    return render(request,tmp,{'registro':registro})

class Home_Admin(LoginRequiredMixin,SuperuserRequiredMixin,TemplateView):
    login_url = '/'
    template_name = u'ModuloAdmin/VentasTemplate/home_admin.html'

    def get_context_data(self, **kwargs):
        #Reporte de Ventas
        context = super(Home_Admin,self).get_context_data(**kwargs)
        tipo = Tipo.objects.all()
        ax=0
        aux = []
        for tipo in tipo:
            prueba = Articulo.objects.filter(nombre_tipo=tipo.pk)
            cont=0
            for prueba in prueba:
                rti = Alquiler_Detail.objects.filter(articulo=prueba.pk).count()
                cont += rti
            ax += cont
            aux.append([tipo.nombre_tipo, cont])
        print(aux)
        context['tipo'] = aux
        context['venta_toal']=ax

        #Reporte Diario
        dia_hoy = date.today()
        reporte_dia = Alquiler.objects.filter(fecha_entrega=dia_hoy)
        reporte_diario = Alquiler.objects.filter(fecha_devolucion=dia_hoy)
        reporte_dia_devolucion = Alquiler.objects.filter(fecha_devolucion_dia=dia_hoy)
        multa_diaria=0
        deposito = 0
        suma = 0
        context['reporte_dia'] = reporte_dia

        for reporte_dia_devolucion in reporte_dia_devolucion:
            multa_diaria += reporte_dia_devolucion.multa

        for reporte_dia in reporte_dia:
            deposito += reporte_dia.deposito
            alquilado = Alquiler_Detail.objects.filter(alquiler=reporte_dia.pk)
            for alquilado in alquilado:
                suma += alquilado.precio-(alquilado.precio*(reporte_dia.descuento/100))

        context['multa'] = multa_diaria
        context['deposito'] = deposito
        context['cantidad'] = Alquiler.objects.filter(fecha_entrega=dia_hoy).count()
        context['suma'] = suma
        context['reporte_diario']=reporte_diario

        #Reservas
        dia_hoy_reserva = date.today()
        dia_max = dia_hoy_reserva+timedelta(days=2)
        context['reservas'] = Reserva.objects.filter(fecha_reserva__range=(dia_hoy,dia_max))
        context['reservas_caducada'] = Reserva.objects.filter(fecha_limite__lt=dia_hoy_reserva).count()
        context['reservas_pen'] = Reserva.objects.filter(fecha_limite__gt=dia_hoy_reserva).count()

        #Reporte Mes
        multa_diaria_mes=0
        deposito_mes = 0
        suma_m = 0
        dia_mes = date(dia_hoy.year,dia_hoy.month,1)
        multa_mes =Alquiler.objects.filter(fecha_devolucion_dia__range=(dia_mes,dia_hoy))
        alquiler_mes = Alquiler.objects.filter(fecha_entrega__range=(dia_mes,dia_hoy))
        for alquiler_mes in alquiler_mes:
            alquiler_mes_detail = Alquiler_Detail.objects.filter(alquiler=alquiler_mes.pk)
            suma_mes=0
            deposito_mes += alquiler_mes.deposito
            for alquiler_mes_detail in alquiler_mes_detail:
                suma_m += alquiler_mes_detail.precio-(alquiler_mes_detail.precio*(alquiler_mes.descuento/100))
        for multa_mes in multa_mes:
            multa_diaria_mes +=multa_mes.multa
        context['multa_diaria_mes']= multa_diaria_mes
        context['deposito_m'] = deposito_mes
        context['cantidad_m'] = Alquiler.objects.filter(fecha_entrega__range=(dia_mes,dia_hoy)).count()
        context['suma_m'] = suma_m
        context['cliente']= Cliente.objects.all().count()
        return context
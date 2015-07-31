from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout
from datetime import date,timedelta

from Apps.Inventario.models import Articulo,Estado_Ropa
from Apps.Alquiler.models import Alquiler,Alquiler_Detail

def login(request):
    tmp='Login.html'
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            dia_max=date.today()-timedelta(days=7)
            dia_min=date.today()-timedelta(days=2)
            cambio_estado = Estado_Ropa.objects.get(pk=1)
            alquiler = Alquiler.objects.filter(devuelto=True,fecha_devolucion__gte=dia_max)
            for alquiler in alquiler:
                if alquiler.fecha_devolucion < dia_min:
                    alquiler_detail = Alquiler_Detail.objects.filter(alquiler=alquiler.pk)
                    for alquiler_detail in alquiler_detail:
                        articulo = Articulo.objects.get(referencia=alquiler_detail.articulo)
                        articulo.nombre_estado_ropa=cambio_estado
                        if articulo.nuevo:
                            articulo.nuevo=False
                            rebaja = (articulo.precio*0.20)
                            articulo.precio = articulo.precio-rebaja
                        articulo.save()
            if user.is_staff:
                return redirect('Inventario:Inventario_Lista')
            else:
                return redirect('Alquiler:Alquiler_Ingresar')
    return render(request,tmp)

def Logout(request):
    logout(request)
    return redirect('User_app:login')
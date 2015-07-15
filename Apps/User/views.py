from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

def login(request):
    tmp='Login.html'
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        username = password = None
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/Gestion/Inventario-Lista/')
    return render(request,tmp)

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
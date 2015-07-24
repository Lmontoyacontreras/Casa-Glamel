from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout

def login(request):
    tmp='Login.html'
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Inventario:Inventario_Lista')
    return render(request,tmp)

def Logout(request):
    logout(request)
    return redirect('User_app:login')
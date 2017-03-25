from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core import serializers
from app.hackaton import models
from django.db.models import Sum, Q, Max, Avg, Count
import os
from datetime import datetime, timedelta

# Create your views here.
def login_view(request):
    return render(request, "login.html")

def index_view(request):
    return HttpResponse("Render Index")

def login_aut(request):
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['usuario_id'] = user.id
            return JsonResponse({'mensaje':'Acceso'})
        else:
            return JsonResponse({'mensaje':'Error'})
    else:
        return redirect('/')

def registro_registrar(request):
    if request.method == "POST":
        array_errores = []
        diccionario = {}
        nombre = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        banera = request.POST.get('banera')
        regadera = request.POST.get('regadera')
        ahorrador = request.POST.get('ahorrador')
        cont = 0
        usuario = User.objects.filter(username=nombre)
        for datos in usuario:
            if datos.email == email:
                array_errores.append("Email ya registrado")
            cont = cont + 1
        if cont == 0:
            usuario = User.objects.create_user(username=nombre, password=password, email=email)
            diccionario["mensaje"] = "Acceso"
            return JsonResponse(diccionario)
        else:
            array_errores.append("Usuario ya registrado")
            diccionario["errores"] = array_errores
        return JsonResponse(diccionario)
    else:
        return redirect('/')

def registro_view(request):
    return render(request, "registro.html")

def profile_view(request):
    return render(request, "profile.html")

def profile_view_modificar(request):
    return render(request, "editar.html")

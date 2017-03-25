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

def registro_view(request):
    return HttpResponse("Hola")

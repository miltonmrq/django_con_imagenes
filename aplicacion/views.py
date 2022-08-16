from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.


def list(request):
    empleados = Empleado.objects.all()
    return render(request, 'list.html', {'empleados': empleados})


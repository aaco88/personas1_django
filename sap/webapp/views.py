from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    cantPersonas = Persona.objects.count()
    # todasPersonas = Persona.objects.all()
    todasPersonas = Persona.objects.order_by('id', 'nombre')
    return render(request, 'bienvenido.html', {'cPersonas': cantPersonas, 'tPersonas': todasPersonas})


def listadoDomicilios(request):
    cantDomicilios = Domicilio.objects.count()
    todosDomicilios = Domicilio.objects.order_by('id')
    return render(request, 'domicilios.html', {'cDomicilios': cantDomicilios, 'tDomicilios': todosDomicilios})
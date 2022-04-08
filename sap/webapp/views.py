from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def bienvenido(request):
    return render(request, 'bienvenido.html', {'msg1': 'Mensaje1', 'msg2': 'Mensaje2'})
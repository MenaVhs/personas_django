from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request): # información de la petición
    return HttpResponse('HOla mundo desede views de webapp')
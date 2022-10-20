from datetime import datetime
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse  

from django.template import loader  

# def saludar(request):
#     return HttpResponse('Hola')

# def saludar_nombre(request,nombre):
#     return HttpResponse(f'<h1>Hola {nombre}</h1>')

def index(request):
    return render(request, 'productos/index.html')

def lista_clases(request):
    _clases_disponibles = [
        { 'nombre' : 'Danza Clasica',
          'descripcion' : 'Es una danza fhfahdfhfdhfhfhfdf',
        #   'Fecha_vencimiento': datetime.now
        },
        
        { 'nombre' : 'Danza Española',
          'descripcion' : 'La danza española surgio en los años 80',
        #   'Fecha_vencimiento': datetime.now
        }
    ]
    
    context = {
        'clases': _clases_disponibles,
        'hoy': datetime.now,
        # 'Fecha_vencimiento': datetime.now
    }
    
    return render(request, 'productos/clase.html', context=context)
  
def galeria(request): 
  return render(request,'productos/galeria.html', context={})

def contacto(request): 
  return render(request,'productos/contacto.html', context={})
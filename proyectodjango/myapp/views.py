from re import template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.template import loader
from myapp.models import Persona 

def crear_familia(request):
    template = loader.get_template("templates1.html")
    familiar_1 = Persona(nombre = 'Pepe', apellido = 'Argento', email = 'pepe@gmail.com', altura = 1.80, fecha_nacimiento = '1978-05-03')
    familiar_1.save()
    familiar_2 = Persona(nombre = 'Moni', apellido = 'Argento', email = 'moni@gmail.com', altura = 1.68, fecha_nacimiento = '1976-07-03')
    familiar_2.save() 
    familiar_3 = Persona(nombre = 'Coki', apellido = 'Argento', email = 'coki@gmail.com',  altura = 1.61, fecha_nacimiento = '1989-04-23')
    familiar_3.save()
    familiar_4 = Persona(nombre = 'Luana', apellido = 'Argento', email = 'luana@gmail.com', altura = 1.68, fecha_nacimiento = '1990-10-22')
    familiar_4.save()
    
    dict_de_contexto = {
        "familiar_1": familiar_1,
        "familiar_2": familiar_2,
        "familiar_3": familiar_3,
        "familiar_4": familiar_4,
    }
    
    res = template.render(dict_de_contexto)
    return HttpResponse(res)
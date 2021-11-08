from time import perf_counter
from django import http
from django.http import HttpResponse
import datetime

#librerias impotadas para leer las plantillas
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #primera vista

    prueba=''
    p1=Persona('Jose','Diaz')
    temas=["Comida","Bebida", "Dormir","Despertar"]
    #nombre='Roberto'
    #apellido='Escobedo'

    ahora=datetime.datetime.now()
    
    #doc_externo=open("D:/proyectos/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    #parte 2
    #doc_externo=get_template('miplantilla.html')

    # Se pasan diccionarios para pasar informacion a la plantilla
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temas})
    
    #parter 2
    #documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temas})

    return render(request,"miplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temas})

def despedida(request):
    return HttpResponse("Hasta luego manito")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    texto="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(texto)

def caculaEdad(request,agno):
    edadActual=18
    periodo=agno-2021
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno,edadFutura)
    return HttpResponse(documento)

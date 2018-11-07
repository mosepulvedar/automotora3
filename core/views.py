from django.shortcuts import render, redirect
from .models import Marca, Automovil
#importamos la mensajeria de django para utilizarla
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
#un decorador nos permite extender la funcionalidad
#de un metodo. en este caso particular le solicitaremos
#primero la autenticacion al usuario para ingresar a un
#view

class ServiceWorker(TemplateView):
    template_name = "core/serviceworker.js"
    content_type = "application/javascript"

def api_listado_autos(request):
    autos = Automovil.objects.prefetch_related('marca')
    
    autosJSON = serializers.serialize('json', autos)

    return HttpResponse(autosJSON, content_type="application/json")

@csrf_exempt
@require_http_methods(['PUT'])
def api_modificar_auto(request):
   
    #primero le hacemos un decode
    body = request.body.decode('utf-8')
    #luego transformamos el string en json
    body = json.loads(body)

    auto = Automovil()
    auto.id = body['id']
    auto.modelo = body['modelo']
    auto.anio = body['anio']
    auto.marca = Marca(id = body['marca_id'])
    auto.patente = body['patente']

    auto.save()

    return HttpResponse(json.dumps({'mensaje':"modificado correctamente"}), content_type="application/json")


@csrf_exempt
def api_agregar_auto(request):
    #primero le hacemos un decode
    body = request.body.decode('utf-8')
    #luego transformamos el string en json
    body = json.loads(body)

    auto = Automovil()
    auto.modelo = body['modelo']
    auto.anio = body['anio']
    auto.marca = Marca(id = body['marca_id'])
    auto.patente = body['patente']

    auto.save()

    

    return HttpResponse(json.dumps({'mensaje':"agregado correctamente"}), content_type="application/json")

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def rest_eliminar(request, id):
    #primer paso encontrar el automovil
    auto = Automovil.objects.get(id=id)

    #una vez encontrado el automovil se elimina
    try:
        auto.delete()
        jsonm = {'mensaje':'eliminado correctamente'}
    except:
        jsonm = {'mensaje':'no se ha podido eliminar'}
    
    #redirigiremos al usuario de vuelta al listado
    return HttpResponse(json.dumps(jsonm), content_type='application/json')


@login_required
def agregar_auto(request):
    #buscaremos todas las marcas
    #y se las enviaremos al template
    marcas = Marca.objects.all()
    variables = {
        'marcas':marcas
    }

    #preguntaremos si la peticion es de tipo POST

    if request.POST:
        #si el request es post obtendremos las variables
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        #crearemos un objeto Marca para obtener el id de la marca
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        #guardamos marca dentro de auto
        auto.marca = marca

        #procederemos a guardar al auto en la BBDD
        try:
            auto.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/agregar_auto.html', variables)


def listar_autos(request):
    #buscamos todos los automoviles
    autos = Automovil.objects.all()

    variables = {
        'autos':autos
    }

    return render(request, 'core/listar_autos.html', variables)

def eliminar_auto(request, id):
    #primer paso encontrar el automovil
    auto = Automovil.objects.get(id=id)

    #una vez encontrado el automovil se elimina
    try:
        auto.delete()
        messages.success(request, 'Eliminado correctamente')
    except:
        messages.error(request, 'No se ha podido eliminar')
    
    #redirigiremos al usuario de vuelta al listado
    return redirect('listar_autos')

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
#el serializer permite transformar un arreglo en un json
from django.core import serializers
import json
from core.models import Estado, Genero, Raza, Mascota

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(['POST'])
def agregar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)
    token = bodyDict['token']
    #Preguntamos si ya existe el token en la base de datos 
    existe = FCMDevice.objects.filter(registration_id = token, active = True)

    if existe:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El Token Ya Existe'}), content_type="application/json")

    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True
    #crearemos un view que muestre el listado de automoviles
    #en formato json
    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Token Guardado Correctamente'}), content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No Se Ha Podido Guardar El Token'}), content_type="application/json")
    

def listar_mascotas(request):
    mascota = Mascota.objects.all()
    #transformamos los datos a json
    mascotaJson = serializers.serialize('json', mascota)

    #mostramos el json en el navegador
    return HttpResponse(mascotaJson, content_type="application/json")

#POST
@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos la mascota en la BBDD
    Masc = Mascota()
    Masc.nombre = bodyDict['nombre']
    Masc.fechaIngreso = bodyDict['fechaIngreso']
    Masc.fechaNacimiento  = bodyDict['fechaNacimiento']

    Masc.Genero = Genero(id=bodyDict['genero_id'])
    Masc.Estado = Estado(id=bodyDict['estado_id'])
    Masc.Raza = Raza(id=bodyDict['raza_id'])

    #Masc.imagen = bodyDict['imagen']

    try:
        Masc.save()
        return HttpResponse(json.dumps({'mensaje':'Guardado correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'No Se Ha Podido Guardar'}), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        #primero buscamos la mascota que eliminaremos
        Masc = Mascota.objects.get(id=id)
        Masc.delete()
        return HttpResponse(json.dumps({'mensaje':'Eliminado Correctamente'}),
         content_type="application/json")
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':"No Se Ha Podido Eliminar"}),
        content_type="application/json")
    

#POST
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtenemos el body del request
    body = request.body.decode('utf-8')
    #el body viene como un string, por lo que lo transformamos
    bodyDict = json.loads(body)

    #guardaremos la mascota en la BBDD
    Masc = Mascota()
    Masc.id = bodyDict['id']
    Masc.nombre = bodyDict['nombre']
    Masc.fechaIngreso = bodyDict['fechaIngreso']
    Masc.fechaNacimiento  = bodyDict['fechaNacimiento']
    Masc.Genero = Genero(id=bodyDict['genero_id'])
    Masc.Estado = Estado(id=bodyDict['estado_id'])
    Masc.Raza = Raza(id=bodyDict['raza_id'])

    try:
        Masc.save()
        return HttpResponse(json.dumps({'mensaje':'Modificado Correctamente'}), content_type="application/json")
    except:
        #retornaremos un mensaje con un codigo de error
        return HttpResponseBadRequest(json.dumps({'mensaje':'No Se Ha Podido Modificar'}), content_type="application/json")


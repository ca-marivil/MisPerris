from django.shortcuts import render, redirect
from .models import Region, Comuna, TipoVivienda, Cliente, Estado, Genero, Raza, Mascota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fcm_django.models import FCMDevice

# Create your views here.

def home(request):
    return render(request, 'core/home.html')
    
def galeria(request):
    return render(request , 'core/galeria.html')

def formulario(request):

    region = Region.objects.all()
    comuna = Comuna.objects.all()
    tipovivienda = TipoVivienda.objects.all()
    variable = {
        'region':region,
        'comuna':comuna,
        'tipovivienda':tipovivienda

    }

    if request.POST:
        cliente = Cliente()
        cliente.rut = request.POST.get('txtrun')
        cliente.nomCompleto = request.POST.get('txtnombre')
        cliente.email = request.POST.get('txtcorreo')
        cliente.fono = request.POST.get('txtnumero')
        cliente.fechaNaci = request.POST.get('dpfecha_nac')
        

        region = Region()
        region.id = request.POST.get('cbo_region')
        cliente.Region = region

        comuna = Comuna()
        comuna.id = request.POST.get('cbo_comuna')
        cliente.Comuna = comuna

        tipovivienda = TipoVivienda()
        tipovivienda.id = request.POST.get('cbo_tipo_vivienda')
        cliente.TipoVivienda = tipovivienda
        
        cliente.save()
        try:
            
            variable['mensaje'] = 'Guardado correctamente'
        except:
            variable['mensaje'] = 'No se ha podido guardar'


    return render(request, 'core/formulario.html', variable)

#CRUD De Mascota

@login_required
def agregar_mascota(request):

    genero = Genero.objects.all()
    estado = Estado.objects.all()
    raza = Raza.objects.all()
    
    variables = {
        'genero':genero,
        'estado':estado,
        'raza':raza
    }
     
    if request.POST:
        Masc = Mascota()
        Masc.nombre = request.POST.get('txtnombre')
        Masc.fechaIngreso = request.POST.get('dpfecha_in')
        Masc.fechaNacimiento = request.POST.get('dpfecha_nac')
        

        genero = Genero()
        genero.id = request.POST.get('cbo_genero')
        Masc.Genero = genero

        estado = Estado()
        estado.id = request.POST.get('cbo_estado')
        Masc.Estado = estado

        raza = Raza()
        raza.id = request.POST.get('cbo_raza')
        Masc.Raza = raza

        Masc.imagen = request.FILES.get('txtImagen')

        Masc.save()
        try:
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/agregar_mascota.html', variables)

@login_required
def listar_mascotas(request):

    mascota = Mascota.objects.all()

    return render(request, 'core/listar_mascotas.html', {'mascota':mascota})

def eliminar_mascota(request, id):
    #Buscar la mascota que queremos eliminar
    mascota = Mascota.objects.get(id=id)

    try:
        mascota.delete()
        mensaje = "Se Ha Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No Se Ha Podido Eliminar"
        messages.error(request, mensaje)

    return redirect('listado_mascotas')

@login_required
def modificar_mascota(request, id):
    #Buscamos la mascota para que el usuario lo pueda modificar
    mascota = Mascota.objects.get(id=id)
    raza = Raza.objects.all()
    genero = Genero.objects.all()
    estado = Estado.objects.all()
    variables = {
        'mascota':mascota,
        'raza':raza,
        'genero':genero,
        'estado':estado,
    }

    if request.POST:
        mascota = Mascota()
        mascota.id = request.POST.get('txtId')
        mascota.nombre = request.POST.get('txtnombre')
        mascota.fechaIngreso = request.POST.get('dpfecha_in')
        mascota.fechaNacimiento = request.POST.get('dpfecha_nac')
        

        genero = Genero()
        genero.id = request.POST.get('cbo_genero')
        mascota.Genero = genero

        estado = Estado()
        estado.id = request.POST.get('cbo_estado')
        mascota.Estado = estado

        raza = Raza()
        raza.id = request.POST.get('cbo_raza')
        mascota.Raza = raza

        mascota.imagen = request.FILES.get('txtImagen')

        try:
            mascota.save()
            messages.success(request, 'Mascota Modificada correctamente')
        except:
            messages.error(request, 'No se ha podido Modificar' )
        return redirect('listado_mascotas')

    return render(request,'core/modificar_mascota.html', variables)

from django.contrib import admin
from .models import Region, Comuna, TipoVivienda, Cliente, Estado, Genero, Raza, Mascota
# Register your models here.

class comunaAdmin(admin.ModelAdmin):
    list_display = ('nomComuna', 'Region')
    list_filter = ('Region',)

class clienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nomCompleto', 'email', 'fono', 'fechaNaci', 'Region', 'Comuna', 'TipoVivienda')
    list_filter = ('TipoVivienda',)

class mascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fechaIngreso', 'fechaNacimiento', 'Raza', 'Genero', 'Estado', 'imagen')
    list_filter = ('Estado',)

admin.site.register(Region)
admin.site.register(Comuna, comunaAdmin)
admin.site.register(TipoVivienda)
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Estado)
admin.site.register(Genero)
admin.site.register(Raza)
admin.site.register(Mascota, mascotaAdmin)
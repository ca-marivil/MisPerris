from django.urls import path
from .views import home, galeria, formulario, agregar_mascota, listar_mascotas, eliminar_mascota, modificar_mascota

urlpatterns =[
    path('',home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('agregar_mascota/', agregar_mascota, name="agregar"),
    path('listar_mascota/', listar_mascotas, name="listado_mascotas"),
    path('eliminar_mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
    path('modificar_mascota/<id>/', modificar_mascota, name="modificar_mascota"),
]
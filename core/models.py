from django.db import models


# Create your models here.
class Region(models.Model):
    nomRegion = models.CharField(max_length=50)
    def __str__(self):
        return self.nomRegion

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"


class Comuna(models.Model):
    nomComuna = models.CharField(max_length = 100, verbose_name ='Comuna' )
    Region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomComuna
    

class TipoVivienda(models.Model):
    descripcion = models.CharField(max_length = 100)
    def __str__(self):
        return self.descripcion


class Cliente(models.Model):
    rut = models.IntegerField(unique = True)
    nomCompleto = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fono = models.IntegerField()
    fechaNaci = models.DateField()
    Comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE, null=True)
    Region = models.ForeignKey(Region, on_delete = models.CASCADE)
    TipoVivienda = models.ForeignKey(TipoVivienda, on_delete = models.CASCADE)

    def str(self):
        return self.nomCompleto

class Estado(models.Model):
    nomEstado = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomEstado
    
class Genero(models.Model):
    nomGenero = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomGenero


class Raza(models.Model):
    nomRaza = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomRaza


class Mascota(models.Model):
    nombre = models.CharField(max_length = 100, unique = True)
    fechaIngreso = models.DateField()
    fechaNacimiento = models.DateField()
    Raza = models.ForeignKey(Raza, on_delete = models.CASCADE)
    Genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = "mascotas", null = True)

    def __str__(self):
        return self.nombre

    def fechaNacimientoC(self):
        return self.fechaNacimiento.strftime("%Y-%m-%d")

    def fechaIngresoC2(self):
        return self.fechaIngreso.strftime("%Y-%m-%d")
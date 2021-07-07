from django.db import models

# Create your models here.

class Paises(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name='Id del Pais')
    nombrePais = models.CharField(max_length=50, verbose_name='Nombre del Pais')

    def __str__(self):
        return self.nombrePais


class Registrarse(models.Model):
    rut_colaborador = models.CharField(max_length=10,primary_key=True, verbose_name='Rut del Colaborador')
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    nombre_completo = models.CharField(max_length=65,verbose_name='Nombre Completo')
    telefono = models.CharField(max_length=9, verbose_name='Telefono')
    dirección = models.CharField(max_length=30, verbose_name='Dirección')
    email = models.CharField(max_length=30, verbose_name='email')
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    contraseña = models.CharField(max_length=30,verbose_name='Contraseña')
    def __str__(self):
        return self.rut_colaborador
__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
from django.db import models

# Create your models here.

class DatosTecnico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    cedula=models.CharField(max_length=8,primary_key=True)
    SEXO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO)
    Telefono=models.CharField(max_length=11)
    correo_corporativo=models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.nombres

class Registro(models.Model):
    tecnico=models.ForeignKey(DatosTecnico, null=True, blank=False, on_delete=models.CASCADE)
    serial=models.CharField(max_length=16)
    fecha =models.DateField()
    historico=models.TextField()

    def __str__(self):
        return self.serial

class Repuesto(models.Model):
    tecnico=models.ForeignKey(DatosTecnico, null=True, blank=False, on_delete=models.CASCADE)
    serial=models.CharField(max_length=16, primary_key=True)
    fecha=models.DateTimeField()
    pantalla=models.BooleanField()
    lector=models.BooleanField()
    memoria_ram=models.BooleanField()
    fan_cooler=models.BooleanField()
    computadora=models.BooleanField()
    ele=models.BooleanField()

    def __str__(self):
        return self.serial










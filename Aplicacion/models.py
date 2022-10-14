from unittest.util import _MAX_LENGTH
from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()

class Doctor(models.Model):
    id_doctor = models.AutoField(primary_key = True)
    nombre_doctor = models.CharField(max_length=50)
    apellido_doctor = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key = True)
    nombre_paciente = models.CharField(max_length=50)
    apellido_paciente = models.CharField(max_length=50)
    fecha_Nac = models.DateField(max_length=50)
    direccion_paciente = models.CharField(max_length=50)
    telefono_paciente = models.IntegerField(max_length=50)
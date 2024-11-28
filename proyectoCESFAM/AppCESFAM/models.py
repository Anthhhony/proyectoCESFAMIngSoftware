from django.db import models
from django.core import validators
from django.core.validators import RegexValidator, EmailValidator, MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator


class TipoDocumento(models.Model):
    id_tipodoc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    tipo = models.CharField(max_length=50)
    direccion = models.TextField()
    contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128)  # Usar hashing para contraseñas
    correo = models.EmailField(unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_tipodoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_ingreso = models.DateField()
    fecha_documento = models.DateField()
    valor_monetario = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Documento {self.id_documento}"


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    estado = models.CharField(max_length=50)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Asignación {self.id_asignacion}"
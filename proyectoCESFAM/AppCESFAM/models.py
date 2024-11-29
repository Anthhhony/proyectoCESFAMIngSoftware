from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class TipoDocumento(models.Model):
    id_tipodoc = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )

    def __str__(self):
        return self.nombre


class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    rut = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}\.\d{3}\.\d{3}-[0-9kK]$',
                message="El RUT debe tener el formato chileno: 12.345.678-9 o 1.234.567-K."
            )
        ]
    )
    tipo = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El tipo solo puede contener letras y espacios."
            )
        ]
    )
    direccion = models.TextField()
    contacto = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{8,15}$',
                message="El número de contacto debe tener entre 8 y 15 dígitos, con o sin prefijo '+' al inicio."
            )
        ]
    )

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    rut = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}\.\d{3}\.\d{3}-[0-9kK]$',
                message="El RUT debe tener el formato chileno: 12.345.678-9 o 1.234.567-K."
            )
        ]
    )
    password = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8, message="La contraseña debe tener al menos 8 caracteres."),
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="La contraseña debe incluir al menos una letra, un número y un símbolo especial."
            )
        ]
    )
    correo = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        validators=[EmailValidator(message="Debe ser un correo válido.")]
    )
    telefono = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{8,15}$',
                message="El número de teléfono debe tener entre 8 y 15 dígitos, con o sin prefijo '+' al inicio."
            )
        ]
    )

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    id_tipodoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_ingreso = models.DateField(
        validators=[]
    )
    fecha_documento = models.DateField()
    valor_monetario = models.DecimalField(max_digits=12, decimal_places=2)

    def clean(self):
        super().clean()
        # Validación personalizada para fecha_ingreso
        if self.fecha_ingreso < now().date():
            raise ValidationError("La fecha de ingreso no puede ser anterior al día de hoy.")

    def __str__(self):
        return f"Documento {self.id_documento}"


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    estado = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El estado solo puede contener letras y espacios."
            )
        ]
    )
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Asignación {self.id_asignacion}"
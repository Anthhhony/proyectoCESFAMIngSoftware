from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now




class TipoDocumento(models.Model):
    id_tipodoc = models.AutoField(primary_key=True)
    # Campo automático para la clave primaria.

    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    # Campo para el nombre del tipo de documento con una longitud máxima de 255 caracteres.
    # Incluye una validación para permitir solo letras y espacios.

    def __str__(self):
        return self.nombre
    # Devuelve el nombre como representación de texto del objeto.


class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    # Campo automático para la clave primaria.

    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    # Campo para el nombre de la institución con validación similar a `TipoDocumento`.

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
    # Campo para el RUT chileno, único para cada institución, con validación de formato.

    tipo = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El tipo solo puede contener letras y espacios."
            )
        ]
    )
    # Campo para el tipo de institución, con validación para solo letras y espacios.

    direccion = models.TextField()
    # Campo para almacenar la dirección en formato de texto.

    contacto = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{8,15}$',
                message="El número de contacto debe tener entre 8 y 15 dígitos, con o sin prefijo '+' al inicio."
            )
        ]
    )
    # Campo para el número de contacto con validación de formato.

    def __str__(self):
        return self.nombre
    # Representación de texto de la institución como su nombre.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    # Clave primaria automática.

    nombre = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El nombre solo puede contener letras y espacios."
            )
        ]
    )
    # Nombre del usuario, con validación para letras y espacios.

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
    # RUT único, validado según el formato chileno.

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
    # Contraseña con requisitos de seguridad.

    correo = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        validators=[EmailValidator(message="Debe ser un correo válido.")]
    )
    # Campo de correo electrónico único, opcional y validado.

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
    # Campo opcional para teléfono, con validación de formato.

    def __str__(self):
        return self.nombre
    # Devuelve el nombre del usuario como su representación textual.


class Documento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    # Clave primaria automática.

    id_tipodoc = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    # Relación con `TipoDocumento`, se elimina el documento si el tipo se elimina.

    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    # Relación con `Institucion`, se elimina el documento si la institución se elimina.

    motivo = models.TextField()
    # Texto que describe el motivo del documento.

    fecha_ingreso = models.DateField()
    # Fecha en la que se ingresa el documento.

    fecha_documento = models.DateField()
    # Fecha original del documento.

    valor_monetario = models.DecimalField(max_digits=12, decimal_places=2)
    # Monto asociado al documento, con hasta 12 dígitos y 2 decimales.

    def clean(self):
        super().clean()
        if self.fecha_ingreso < now().date():
            raise ValidationError("La fecha de ingreso no puede ser anterior al día de hoy.")
    # Validación personalizada para asegurar que `fecha_ingreso` no sea pasada.

    def __str__(self):
        return f"Documento {self.id_documento}"
    # Representación textual del documento.


class Asignacion(models.Model):
    id_asignacion = models.AutoField(primary_key=True)
    # Clave primaria automática.

    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # Relación con `Usuario`, se elimina la asignación si el usuario se elimina.

    id_documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
    # Relación con `Documento`, se elimina la asignación si el documento se elimina.

    fecha_asignacion = models.DateField()
    # Fecha en la que se asigna el documento.

    estado = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El estado solo puede contener letras y espacios."
            )
        ]
    )
    # Estado de la asignación, validado para solo letras y espacios.

    nota = models.TextField(blank=True, null=True)
    # Campo opcional para notas adicionales.

    def __str__(self):
        return f"Asignación {self.id_asignacion}"
    # Representación textual de la asignación.
    
class Alerta(models.Model):
    documento = models.OneToOneField('Documento', on_delete=models.CASCADE)
    # Relación uno a uno con `Documento`, se elimina la alerta si el documento se elimina.

    fecha_alerta = models.DateField(auto_now_add=True)
    # Fecha de creación de la alerta, asignada automáticamente.

    mensaje = models.TextField(default="Documento vencido")
    # Mensaje de la alerta, con valor predeterminado.

    def __str__(self):
        return f"Alerta para Documento {self.documento.id_documento}"
    # Representación textual de la alerta.
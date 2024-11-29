from django.contrib import admin
from .models import TipoDocumento, Institucion, Usuario, Documento, Asignacion


@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_tipodoc', 'nombre')  # Campos a mostrar en la lista
    search_fields = ('nombre',)  # Habilitar búsqueda por nombre
    ordering = ('id_tipodoc',)  # Orden por defecto


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('id_institucion', 'nombre', 'rut', 'tipo', 'contacto')  # Campos visibles
    search_fields = ('nombre', 'rut')  # Búsqueda por nombre o RUT
    list_filter = ('tipo',)  # Filtros por tipo
    ordering = ('id_institucion',)  # Orden por defecto


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'rut', 'correo', 'telefono')  # Campos visibles
    search_fields = ('nombre', 'rut', 'correo')  # Búsqueda por nombre, RUT o correo
    list_filter = ('rut',)  # Filtros (si aplica)
    ordering = ('id_usuario',)  # Orden por defecto


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id_documento', 'id_tipodoc', 'id_institucion', 'motivo', 'fecha_ingreso', 'fecha_documento', 'valor_monetario')
    search_fields = ('id_documento', 'motivo')  # Habilitar búsqueda
    list_filter = ('fecha_ingreso', 'id_tipodoc')  # Filtros por fecha y tipo de documento
    ordering = ('fecha_ingreso',)  # Ordenar por fecha de ingreso


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('id_asignacion', 'id_usuario', 'id_documento', 'fecha_asignacion', 'estado')  # Campos visibles
    search_fields = ('id_asignacion', 'estado')  # Búsqueda por ID de asignación o estado
    list_filter = ('estado', 'fecha_asignacion')  # Filtros por estado y fecha de asignación
    ordering = ('id_asignacion',)  # Ordenar por defecto
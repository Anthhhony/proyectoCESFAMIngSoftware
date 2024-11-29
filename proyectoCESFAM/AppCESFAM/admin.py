from django.contrib import admin
from AppCESFAM.models import Libro, Categoria, Cliente, Prestamo, Usuario, Documento,Institucion

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('isbn','titulo', 'autor', 'editorial', 'anio_publicacion', 'disponibilidad', 'usuario')
    list_filter = ('disponibilidad',)
    search_fields = ('titulo', 'isbn')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo', 'usuario')
    search_fields = ('nombre', 'correo')
    
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'contrasena')
    search_fields = ('rut',)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('fecha_prestamo', 'fecha_devolucion', 'estado', 'cliente', 'libro', 'categoria', 'usuario')
    search_fields = ('cliente', 'fecha_prestamo', 'usuario')

class docAdmin(admin.ModelAdmin):
    list_display = (
        'tipo_documento',
        'motivo_documento',
        'fecha_ingreso',
        'fecha_documento',
        'valor_monetario',
        'observacion',
        'archivo_adjunto',
        'institucion_id',
    )


@admin.register(Institucion)
class institucionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'tipo', 'direccion','contacto')
    search_fields = ('nombre', 'rut')


admin.site.register(Documento,docAdmin)
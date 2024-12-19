from django.test import TestCase, Client
from django.urls import reverse
from AppCESFAM.models import Usuario, Documento, Institucion, TipoDocumento, Alerta
from django.contrib.auth.hashers import make_password
from datetime import date
from django.utils.timezone import now

class ViewsTests(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = Usuario.objects.create(
            rut="12345678-9",
            nombre="Test User",
            correo="test@example.com",
            telefono="987654321",
            password=make_password("password123")
        )
        # Crear instituciones y documentos
        self.institucion = Institucion.objects.create(
            nombre="Institución Prueba",
            direccion="Calle Falsa 123"
        )
        self.documento = Documento.objects.create(
            id_documento=1,
            nombre="Documento de Prueba",
            descripcion="Descripción",
            fecha_documento=date.today(),
            id_institucion=self.institucion
        )
        # Cliente para realizar peticiones
        self.client = Client()

def test_login_correcto(self):
    response = self.client.post(reverse('buscar-usuario'), {
        'rut': '12345678-9',
        'password': 'password123'
    })
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "templatesApp/menu.html")

def test_login_incorrecto(self):
    response = self.client.post(reverse('buscar-usuario'), {
        'rut': '12345678-9',
        'password': 'wrongpassword'
    })
    self.assertEqual(response.status_code, 302)  # Redirige por error
    self.assertRedirects(response, reverse('buscar-usuario'))

def test_register_usuario_exitoso(self):
    response = self.client.post(reverse('registrar-usuario'), {
        'rut': '98765432-1',
        'nombre': 'Nuevo Usuario',
        'correo': 'nuevo@example.com',
        'telefono': '123456789',
        'password': 'password123',
        'password2': 'password123'
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('buscar-usuario'))
    self.assertTrue(Usuario.objects.filter(rut='98765432-1').exists())

def test_lista_documentos(self):
    response = self.client.get(reverse('lista-documentos'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "templatesApp/documentos.html")
    self.assertEqual(len(response.context['documentos']), 1)  # Documento creado en setUp

def test_agregar_documento_exitoso(self):
    response = self.client.post(reverse('agregar-doc'), {
        'nombre': 'Nuevo Documento',
        'descripcion': 'Descripción Nueva',
        'id_institucion': self.institucion.id_institucion
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-documentos'))
    self.assertTrue(Documento.objects.filter(nombre='Nuevo Documento').exists())

def test_lista_instituciones(self):
    Institucion.objects.create(nombre='Institución 1', direccion='Dirección 1')
    Institucion.objects.create(nombre='Institución 2', direccion='Dirección 2')
    response = self.client.get(reverse('lista-instituciones'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'templatesApp/instituciones.html')
    self.assertEqual(len(response.context['instituciones']), 2)

def test_agregar_institucion_exitoso(self):
    response = self.client.post(reverse('agregar-institucion'), {
        'nombre': 'Institución de prueba',
        'direccion': 'Calle Falsa 123'
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-instituciones'))
    self.assertTrue(Institucion.objects.filter(nombre='Institución de prueba').exists())

def test_editar_institucion(self):
    institucion = Institucion.objects.create(nombre='Institución Editar', direccion='Antigua')
    response = self.client.post(reverse('editar-institucion', args=[institucion.id_institucion]), {
        'nombre': 'Institución Editada',
        'direccion': 'Nueva Dirección'
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-instituciones'))
    institucion.refresh_from_db()
    self.assertEqual(institucion.nombre, 'Institución Editada')

def test_eliminar_institucion(self):
    institucion = Institucion.objects.create(nombre='Institución Eliminar', direccion='Eliminar Dirección')
    response = self.client.post(reverse('eliminar-institucion', ags=[institucion.id_institucion]))
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-instituciones'))
    self.assertFalse(Institucion.objects.filter(id_institucion=institucion.id_institucion).exists())

def test_editar_documento(self):
    # Crear un documento para editar
    documento = Documento.objects.create(
        id_documento=2,
        nombre="Documento para Editar",
        descripcion="Descripción Antigua",
        fecha_documento=date.today(),
        id_institucion=self.institucion
    )
    # Realizar la edición
    response = self.client.post(reverse('editar-doc', args=[documento.id_documento]), {
        'nombre': 'Documento Editado',
        'descripcion': 'Descripción Nueva',
        'id_institucion': self.institucion.id_institucion
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-documentos'))
    # Verificar que los cambios se guardaron
    documento.refresh_from_db()
    self.assertEqual(documento.nombre, 'Documento Editado')
    self.assertEqual(documento.descripcion, 'Descripción Nueva')

def test_eliminar_documento(self):
    # Crear un documento para eliminar
    documento = Documento.objects.create(
        id_documento=3,
        nombre="Documento para Eliminar",
        descripcion="Descripción a eliminar",
        fecha_documento=date.today(),
        id_institucion=self.institucion
    )
    # Realizar la eliminación
    response = self.client.post(reverse('eliminar-doc', args=[documento.id_documento]))
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('lista-documentos'))
    # Verificar que el documento ya no existe
    self.assertFalse(Documento.objects.filter(id_documento=documento.id_documento).exists())

def test_verificar_documentos_vencidos(self):
    # Crear documentos vencidos y no vencidos
    documento_vencido = Documento.objects.create(
        id_documento=4,
        nombre="Documento Vencido",
        descripcion="Descripción Vencido",
        fecha_documento=date.today().replace(year=2000),  # Fecha pasada
        id_institucion=self.institucion
    )
    documento_no_vencido = Documento.objects.create(
        id_documento=5,
        nombre="Documento No Vencido",
        descripcion="Descripción No Vencido",
        fecha_documento=date.today(),
        id_institucion=self.institucion
    )
    # Verificar documentos vencidos
    response = self.client.get(reverse('verificar-documentos-vencidos'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'templatesApp/alertas.html')
    # Verificar que se generó la alerta para el documento vencido
    self.assertTrue(Alerta.objects.filter(documento=documento_vencido).exists())
    # Verificar que no se generó alerta para el documento no vencido
    self.assertFalse(Alerta.objects.filter(documento=documento_no_vencido).exists())

def test_lista_asignaciones(self):
    # Crear asignaciones (si es necesario)
    # Actualmente, la vista no tiene lógica para mostrar datos específicos
    response = self.client.get(reverse('lista-asignaciones'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'templatesApp/asignaciones.html')




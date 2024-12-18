"""proyectoCESFAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
        # path('editarLibro/<int:pk>', editar_libro, name='editar-libro'),
    # path('eliminarLibro/<int:pk>', eliminar_libro, name='eliminar-libro')
"""
from django.contrib import admin
from django.urls import path
from AppCESFAM.views import vista, lista_documentos, lista_asignaciones, lista_instituciones, register, buscar_usuario, agregarDoc,agregarInstitucion, agregarTipoDoc, editarDoc, eliminarDoc, editarInstitucion, eliminarInstitucion, verificar_documentos_vencidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='registrar-usuario'),#
    path('', buscar_usuario, name='buscar-usuario'),#
    path('menu/', vista, name='menu-principal'),#
    path('Documentos/', lista_documentos , name='lista-documentos'),#
    path('agregarDocumento/', agregarDoc , name='agregar-documentos'),#
    path('EditarDocumento/<int:id>/', editarDoc , name='editar-documento'),#
    path('EliminarDocumento/<int:id>/', eliminarDoc, name='eliminar-documento'),#
    path('asignaciones/', lista_asignaciones, name='lista-asignaciones'),#
    path('Instituciones/', lista_instituciones , name='lista-instituciones'),
    path('agregarInstituciones/', agregarInstitucion, name='agregar-institucion'),
    path('editarInstitucion/<int:id>/', editarInstitucion, name='editar-institucion'),####
    path('eliminarInstitucion/<int:id>/', eliminarInstitucion, name='eliminar-institucion'),####
    path('agregarTipoDoc/', agregarTipoDoc, name='agregar-tipodoc'),#
    path('alertas/', verificar_documentos_vencidos, name='lista-alertas'),#
]
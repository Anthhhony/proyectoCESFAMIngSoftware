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
from AppCESFAM.views import vista, lista_documentos, lista_asignaciones, lista_instituciones, register, buscar_usuario, lista_alertas, agregarDoc,agregarInstitucion, editarDoc, eliminarDoc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='registrar-usuario'),
    path('', buscar_usuario, name='buscar-usuario'),
    path('menu/', vista, name='menu-principal'),
    path('Documentos/', lista_documentos , name='lista-documentos'),
    path('agregarDocumento/', agregarDoc , name='agregar-documentos'),#
    path('editarDocumento/<int:pk>', editarDoc, name='editar-documento'),
    path('eliminarDocumento/<int:pk>', eliminarDoc, name='eliminar-documento'),
    path('asignaciones/', lista_asignaciones, name='lista-asignaciones'),#
    path('Instituciones/', lista_instituciones , name='lista-instituciones'),
    path('agregarInstitucion/', agregarInstitucion, name='agregar-institucion'),#
    path('alertas/', lista_alertas, name='lista-alertas'),#
]
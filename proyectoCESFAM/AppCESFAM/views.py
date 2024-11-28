from datetime import date
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from AppCESFAM.models import Cliente, Libro, models, Prestamo, Categoria, Usuario,Documento
from AppCESFAM.forms import ClienteForm, LibroForm,FormularioDoc 
from . import forms
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def login(request):
    return render(request, "templatesApp/inicio.html")

def vista(request):
    return render(request,"templatesApp/menu.html")

def buscar_usuario(request):
    if request.method == "POST":
        rut = request.POST.get('rut')
        contrasena = request.POST.get('contrasena')
        
        usuario = Usuario.objects.filter(rut=rut).first()
        
        if usuario and check_password(contrasena, usuario.contrasena):
            return render(request, "templatesApp/menu.html")
        else:
            messages.error(request, "R.U.N o contraseña incorrecta.")
            return redirect('buscar-usuario')
            
    return render(request, "templatesApp/inicio.html")

        
def register(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        contrasena = request.POST.get('contrasena')
        password2 = request.POST['password2']

        if contrasena != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('registrar-usuario')

        # Verificar si el RUT ya existe en la base de datos
        if Usuario.objects.filter(rut=rut).exists():
            messages.error(request, "Este R.U.N ya está registrado.")
            return redirect('registrar-usuario')

        # Crear el nuevo usuario con contraseña encriptada
        if not Usuario.objects.filter(rut=rut).exists():
            usuario = Usuario(rut=rut, contrasena=make_password(contrasena))
            usuario.save()
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect('buscar-usuario')

    return render(request, 'templatesApp/registro_inicio.html')

def agregarDoc(request):
    
    if request.method == 'POST':
        form = forms.FormularioDoc(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return lista_documentos(request)
        else:
            form = FormularioDoc()
            
    data = {'form': form}
    return render(request, 'templatesApp/documentos.html', data)

def lista_documentos(request):
    documentos = Documento.objects.all()
    data = {'documentos': documentos}
    return render(request, 'templatesApp/documentos.html',data)


def lista_asignaciones(request):

    return render(request, 'templatesApp/asignaciones.html')

    
def lista_instituciones(request):

    return render(request, 'templatesApp/instituciones.html')


def lista_alertas(request):

    return render(request, 'templatesApp/alertas.html')



    



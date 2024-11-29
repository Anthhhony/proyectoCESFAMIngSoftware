from datetime import date
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from AppCESFAM.models import Usuario
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
        password = request.POST.get('password')
        
        usuario = Usuario.objects.filter(rut=rut).first()
        
        if usuario and check_password(password, usuario.password):
            return render(request, "templatesApp/menu.html")
        else:
            messages.error(request, "R.U.N o contraseña incorrecta.")
            return redirect('buscar-usuario')
            
    return render(request, "templatesApp/inicio.html")

        
def register(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')  # Capturar el nombre
        correo = request.POST.get('correo')  # Capturar el correo
        telefono = request.POST.get('telefono')  # Capturar el teléfono
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Validar contraseñas
        if password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect('registrar-usuario')

        # Verificar si el RUT ya existe
        if Usuario.objects.filter(rut=rut).exists():
            messages.error(request, "Este R.U.N ya está registrado.")
            return redirect('registrar-usuario')

        # Verificar si el correo ya está en uso
        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, "Este correo ya está registrado.")
            return redirect('registrar-usuario')

        # Validar que el teléfono contenga solo números y tenga el largo correcto
        if not telefono.isdigit() or len(telefono) not in [9, 10]:
            messages.error(request, "El número de teléfono debe contener 9 o 10 dígitos.")
            return redirect('registrar-usuario')

        # Crear el nuevo usuario
        usuario = Usuario(
            rut=rut,
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            password=make_password(password)  # Encriptar la contraseña
        )
        usuario.save()
        messages.success(request, "Usuario registrado exitosamente.")
        return redirect('buscar-usuario')

    return render(request, 'templatesApp/registro_inicio.html')


def lista_documentos(request):

    return render(request, 'templatesApp/documentos.html')


def lista_asignaciones(request):


    return render(request, 'templatesApp/asignaciones.html')

    
def lista_instituciones(request):

    return render(request, 'templatesApp/instituciones.html')


def lista_alertas(request):

    return render(request, 'templatesApp/alertas.html')



    



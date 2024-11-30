from datetime import date
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from AppCESFAM.models import Usuario, Documento, Asignacion, TipoDocumento, Institucion, Alerta
from . import forms
from django.utils.timezone import now
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from AppCESFAM.forms import FormularioAsignacion, FormularioDoc, FormularioInstitucion, FormularioRegister, FormularioTipoDoc, formularioLogin

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

def formulario_generico(request, form_class, titulo, redirigir_url, opciones_redirigir=None):
    form = form_class()
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            if opciones_redirigir:
                for field, opciones in opciones_redirigir.items():
                    valor_seleccionado = form.cleaned_data.get(field)
                    if valor_seleccionado in opciones:
                        return redirect(opciones[valor_seleccionado])
            form.save()
            if 'guardar_agregar_otro' in request.POST:
                return redirect(request.path)
            return redirect(redirigir_url)
    return render(request, 'templatesApp/formularios.html', {
        'form':form,
        'titulo':titulo,
        'redirigir_url': redirigir_url
    })

def agregarDoc(request):
    return formulario_generico(
        request,
        forms.FormularioDoc,
        "Agregar Documento",
        'lista-documentos',
        opciones_redirigir={
            'id_tipodoc':{
                'agregar': 'agregar-tipo-documento'
            },
            'id_institucion':{
                'agregar': 'agregar-institucion'
            }
        }
    )

def agregarInstitucion(request):
    return formulario_generico(
        request,
        forms.FormularioInstitucion,
        "Agregar Institución",
        'lista-instituciones'
    )

def agregarTipoDoc(request):
    return formulario_generico(
        request,
        forms.FormularioTipoDoc,
        "Agregar Tipo de Documento",
        'agregar-documentos'
    )

def editarDoc(request, id):
    documento = get_object_or_404(Documento, id_documento=id)
    titulo = 'Editar Documento'
    
    if request.method == 'POST':
        form = FormularioDoc(request.POST, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('lista-documentos')  # Ajusta el nombre de la URL según tu configuración
    else:
        form = FormularioDoc(instance=documento)  # Siempre define `form` para GET
    
    return render(request, 'templatesApp/formularios.html', {
        'form': form,
        'documento': documento,
        'titulo': titulo,
    })

def eliminarDoc(request, id):
    documento = get_object_or_404(Documento, id_documento=id)
    if request.method == 'POST':
        documento.delete()
        return redirect(lista_documentos)
    return render(request, 'templatesApp/eliminar_confirmacion.html', {'documento': documento})
        


def lista_documentos(request):
    documentos = Documento.objects.all()
    data = {'documentos': documentos}
    return render(request, 'templatesApp/documentos.html', data)

def crear_asignacion(request):
        return formulario_generico(
            request,
            forms.FormularioAsignacion,
            "Agregar Asignación",
            'lista-asignaciones'
    )

def actualizar_asignacion(request, pk):
    asignacion = get_object_or_404(Asignacion, pk=pk)
    titulo = 'Editar Asignación'
    if request.method == "POST":
        formulario = FormularioAsignacion(request.POST, instance=asignacion)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_asignaciones')
    else:
        formulario = FormularioAsignacion(instance=asignacion)
    return render(request, 'templatesApp/formularios.html', {'formulario': formulario, 'titulo':titulo, 'asignacion':asignacion})



def lista_asignaciones(request):
    asignaciones = Asignacion.objects.all()
    return render(request, 'templatesApp/asignaciones.html', {'asignaciones': asignaciones})


    
def lista_instituciones(request):
    instituciones = Institucion.objects.all()
    data = {'instituciones': instituciones}
    return render(request,'templatesApp/instituciones.html', data)

####

def editarInstitucion(request, id):
    institucion = get_object_or_404(Institucion, id_institucion=id)
    titulo = 'Editar Institución'
    if request.method == 'POST':
        form = FormularioInstitucion(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('lista-instituciones')  # Redirigir a la lista de instituciones
    else:
        form = FormularioInstitucion(instance=institucion)
    return render(request, 'templatesApp/formularios.html', {
        'form': form,
        'institucion': institucion,
        'titulo': titulo,
    })

def eliminarInstitucion(request, id):
    institucion = get_object_or_404(Institucion, id_institucion=id)
    if request.method == 'POST':
        institucion.delete()
        return redirect('lista-instituciones')  # Redirigir a la lista de instituciones
    return render(request, 'templatesApp/eliminar_confirmacion.html', {'institucion': institucion})


#####


def verificar_documentos_vencidos(request):
    # Obtener los documentos cuya fecha actual ha sobrepasado su fecha estipulada
    documentos_vencidos = Documento.objects.filter(fecha_documento__lt=now().date())

    # Registrar las alertas para cada documento vencido
    for documento in documentos_vencidos:
        # Verificar si ya existe una alerta para evitar duplicados
        if not Alerta.objects.filter(documento=documento).exists():
            Alerta.objects.create(
                documento=documento,
                mensaje=f"El documento con ID {documento.id_documento} ha vencido."
            )

    # Obtener todas las alertas para mostrar en el template
    alertas = Alerta.objects.all()
    return render(request, 'templatesApp/alertas.html', {'alertas': alertas})

def verificar_documentos_vencidos(request):

    documentos_vencidos = Documento.objects.filter(fecha_documento__lt=now().date())


    for documento in documentos_vencidos:

        if not Alerta.objects.filter(documento=documento).exists():
            Alerta.objects.create(
                documento=documento,
                mensaje=f"El documento con ID {documento.id_documento} ha vencido."
            )


    alertas = Alerta.objects.all()
    return render(request, 'templatesApp/alertas.html', {'alertas': alertas})


    



from django import forms
from AppCESFAM.models import Usuario, Libro, Cliente,Documento

class formularioLogin(forms.Form):
    rut = forms.CharField(max_length=12)
    contrasena = forms.CharField(max_length=100)



class FormularioRegister(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['isbn', 'titulo', 'autor', 'editorial', 'anio_publicacion', 'disponibilidad', 'usuario']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'correo', 'usuario']


class FormularioDoc(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
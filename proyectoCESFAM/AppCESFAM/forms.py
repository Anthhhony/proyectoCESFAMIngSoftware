from django import forms
from AppCESFAM.models import Usuario, Documento, Institucion, TipoDocumento, Asignacion

class formularioLogin(forms.Form):
    rut = forms.CharField(max_length=12)
    contrasena = forms.CharField(max_length=100)



class FormularioRegister(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"
        
class FormularioDoc(forms.ModelForm):
    class Meta:
        model = Documento
        fields = "__all__"
        widgets = {
            'id_tipodoc': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_institucion': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'motivo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el motivo del documento',
                    'rows': 3,
                }
            ),
            'fecha_ingreso': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'fecha_documento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'valor_monetario': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor monetario',
                    'step': '0.01',
                }
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_tipodoc'].label = "Tipo de documento"
        self.fields['id_institucion'].label = "Institución"
        
        self.fields['id_tipodoc'].empty_label = None
        self.fields['id_tipodoc'].choices = [('', '--- Seleccione una opción ---')] + list(
            self.fields['id_tipodoc'].choices
        ) + [('agregar', 'Agregar tipo de documento')]
        
        self.fields['id_institucion'].empty_label = None
        self.fields['id_institucion'].choices = [('', '--- Seleccione una opción ---')] + list(
            self.fields['id_institucion'].choices
        ) + [('agregar', 'Agregar Institución')]
        
        
class FormularioInstitucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = "__all__"
        widgets = {
                'nombre': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Nombre de la institución',
                        'maxlength': 255,
                    }
                ),
                'rut': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Formato: 12.345.678-9',
                        'maxlength': 12,
                    }
                ),
                'tipo': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Tipo de institución',
                        'maxlength': 50,
                    }
                ),
                'direccion': forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Dirección de la institución',
                        'rows': 3,
                    }
                ),
                'contacto': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Número de contacto (+56912345678)',
                        'maxlength': 20,
                    }
                )
            }
        
class FormularioTipoDoc(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del tipo de documento',
                    'maxlength': 255,
                }
            )
        }
        
class FormularioAsignacion(forms.ModelForm):
    model = Asignacion
    fields = "__all_"
    widgets = {
            'id_usuario': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'id_documento': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha_asignacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'estado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el estado de la asignación',
                    'maxlength': 50,
                }
            ),
            'nota': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Notas adicionales (opcional)',
                    'rows': 3,
                }
            )
        }
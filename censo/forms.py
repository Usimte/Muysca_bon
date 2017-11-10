from django import forms
from .models import censo_archivo, registro_censo


class upload_archivo_censo(forms.ModelForm):

    class Meta():
        model = censo_archivo
        fields = ['archivo', 'fecha_censo']

    def __init__(self, *args, **kwargs):
        super(upload_archivo_censo, self).__init__(*args, **kwargs)
        self.fields['fecha_censo'].widget.attrs['class'] = 'datepicker'


class form_registro_censo(forms.ModelForm):

    class Meta():
        model = registro_censo
        fields = ['resguardo',
                  'comunidad_indigena', 'familia',
                  'tipo_identificacion', 'numero_documento',
                  'nombres', 'apellidos',
                  'fecha_nacimiento', 'parentesco',
                  'genero', 'estado_civil',
                  'profesion', 'escolaridad',
                  'integrantes', 'direccion',
                  'telefono', 'usuario']

    def __init__(self, *args, **kwargs):
        super(form_registro_censo, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.attrs['class'] = 'datepicker'

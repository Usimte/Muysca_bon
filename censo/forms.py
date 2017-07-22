from django import forms
from .models import censo_archivo


class upload_archivo_censo(forms.ModelForm):

    class Meta():
        model = censo_archivo
        fields = ['archivo', 'fecha_censo']

    def __init__(self, *args, **kwargs):
        super(upload_archivo_censo, self).__init__(*args, **kwargs)
        self.fields['fecha_censo'].widget.attrs['class'] = 'datepicker'

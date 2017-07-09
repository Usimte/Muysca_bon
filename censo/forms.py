from django import forms
from .models import Registro_censo


class create_registro_censo(forms.ModelForm):

    class Meta():
        model = Registro_censo
        fields = []

    def __init__(self, *args, **kwargs):
        super(create_sr, self).__init__(*args, **kwargs)

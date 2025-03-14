from django import forms
from .models import MRI

class MRIForm(forms.ModelForm):
    class Meta:
        model = MRI
        fields = [
            'cliente',
            'documento',
            'fecha',
            'descripcion',
            #'dateTime',
        ]

        labels = {
            'cliente' : 'Cliente',
            'documento' : 'Documento',
            'fecha' : 'Fecha',
            'descripcion' : 'Descripcion',
            #'dateTime' : 'Date Time',
        }

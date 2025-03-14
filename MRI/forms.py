from django import forms
from .models import MRI

class MRIForm(forms.ModelForm):
    class Meta:
        model = MRI
        fields = [
            'cliente',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'cliente' : 'Cliente',
            'fecha' : 'Fecha',
            'hora' : 'Hora',
            'descripcion' : 'Descripcion',
            #'dateTime' : 'Date Time',
        }

from rest_framework import serializers
from . import models


class MRISerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'cliente', 'documento', 'fecha', 'descripcion', 'time',)
        model = models.MRI
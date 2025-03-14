from django.db import models
from cliente.models import Cliente

class MRI(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=None)
    documento = models.FloatField(null=True, blank=True, default=None)
    fecha = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
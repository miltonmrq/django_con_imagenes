from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField


class Empleado(models.Model):
    email = models.EmailField(max_length=255)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='aplicacion/static/images', height_field=None, width_field=None, max_length=100)
    descripcion = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.email
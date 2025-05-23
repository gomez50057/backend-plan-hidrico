from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


def validar_pdf(archivo):
    if not archivo.name.endswith('.pdf'):
        raise ValidationError('Solo se permiten archivos PDF.')
    if archivo.size > 5 * 1024 * 1024:
        raise ValidationError('El archivo no debe superar los 5MB.')

class DocumentoCiudadano(models.Model):
    nombre_documento = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    autor = models.CharField(max_length=255)
    fecha_carga = models.DateTimeField(default=timezone.now)
    categorias = models.ManyToManyField(Categoria, related_name='documentos')
    archivo_pdf = models.FileField(upload_to='documentos/pdf/', validators=[validar_pdf])

    def __str__(self):
        return self.nombre_documento

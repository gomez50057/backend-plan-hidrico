from django.contrib import admin
from .models import DocumentoCiudadano, Categoria

@admin.register(DocumentoCiudadano)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_documento', 'autor', 'fecha_carga')
    search_fields = ('nombre_documento', 'autor')
    list_filter = ('fecha_carga', 'categorias')

admin.site.register(Categoria)

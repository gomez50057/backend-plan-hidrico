from rest_framework import serializers
from .models import DocumentoCiudadano, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class DocumentoCiudadanoSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True, read_only=True)
    categoria_ids = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(),
        many=True,
        write_only=True,
        source='categorias'
    )

    class Meta:
        model = DocumentoCiudadano
        fields = [
            'id', 'nombre_documento', 'descripcion', 'autor',
            'fecha_carga', 'archivo_pdf', 'categorias', 'categoria_ids'
        ]
        read_only_fields = ['fecha_carga']
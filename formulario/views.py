from rest_framework import viewsets
from .models import NivelacionTierra, ArchivoPDF
from .serializers import NivelacionTierraSerializer, ArchivoPDFSerializer

class NivelacionTierraViewSet(viewsets.ModelViewSet):
    queryset = NivelacionTierra.objects.all()
    serializer_class = NivelacionTierraSerializer

class ArchivoPDFViewSet(viewsets.ModelViewSet):
    queryset = ArchivoPDF.objects.all()
    serializer_class = ArchivoPDFSerializer

class NivelacionTierraViewSet(viewsets.ModelViewSet):
    """
    Con lookup_field='folio' el router creará:
      - GET   /formularios/           → lista
      - GET   /formularios/{folio}/   → detalle por folio
      - PUT, PATCH, DELETE sobre /formularios/{folio}/
    """
    queryset = NivelacionTierra.objects.all()
    serializer_class = NivelacionTierraSerializer

    # Aquí indicamos que la parte dinámica de la URL es el campo `folio`
    lookup_field = 'folio'
    # Opcional: un regex para los foliios (evita caracteres “/” en el folio)
    lookup_value_regex = '[^/]+'

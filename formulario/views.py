from rest_framework import viewsets
from .models import NivelacionTierra, ArchivoPDF
from .serializers import NivelacionTierraSerializer, ArchivoPDFSerializer

class NivelacionTierraViewSet(viewsets.ModelViewSet):
    queryset = NivelacionTierra.objects.all()
    serializer_class = NivelacionTierraSerializer

class ArchivoPDFViewSet(viewsets.ModelViewSet):
    queryset = ArchivoPDF.objects.all()
    serializer_class = ArchivoPDFSerializer

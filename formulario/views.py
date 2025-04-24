from rest_framework import viewsets
from .models import NivelacionTierra, ArchivoPDF
from .serializers import NivelacionTierraSerializer, ArchivoPDFSerializer
from rest_framework.permissions import IsAuthenticated

class NivelacionTierraViewSet(viewsets.ModelViewSet):
    queryset = NivelacionTierra.objects.all()
    serializer_class = NivelacionTierraSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Guarda el usuario autenticado en created_by
        serializer.save(created_by=self.request.user)

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
    permission_classes = [IsAuthenticated]

    # Aquí indicamos que la parte dinámica de la URL es el campo `folio`
    lookup_field = 'folio'
    lookup_value_regex = '[^/]+'  # evita “/” en el folio

    def perform_create(self, serializer):
        # Guarda el usuario autenticado en created_by
        serializer.save(created_by=self.request.user)

class NivelacionTierraUserViewSet(viewsets.ModelViewSet):
    """
    Lista, crea, detalla, actualiza y borra solo las nivelaciones
    cuyo campo `created_by` es el usuario autenticado.
    
    Rutas generadas:
      - GET    /nivelaciones/          → lista de sus propios registros
      - POST   /nivelaciones/          → crear uno nuevo (se asigna created_by automáticamente)
      - GET    /nivelaciones/{pk}/     → detalle de uno propio
      - PUT    /nivelaciones/{pk}/     → actualizar (solo si es suyo)
      - PATCH  /nivelaciones/{pk}/
      - DELETE /nivelaciones/{pk}/     → eliminar (solo si es suyo)
    """
    serializer_class = NivelacionTierraSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra la lista para que solo aparezcan sus propias instancias
        return NivelacionTierra.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Al crear, asignamos siempre el usuario autenticado
        serializer.save(created_by=self.request.user)

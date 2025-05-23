from rest_framework import generics
from .models import DocumentoCiudadano
from .serializers import DocumentoCiudadanoSerializer
from rest_framework.permissions import AllowAny


class DocumentoListCreateAPIView(generics.ListCreateAPIView):
    queryset = DocumentoCiudadano.objects.all().order_by('-fecha_carga')
    serializer_class = DocumentoCiudadanoSerializer
    permission_classes = [AllowAny]


class DocumentoDetailAPIView(generics.RetrieveAPIView):
    queryset = DocumentoCiudadano.objects.all()
    serializer_class = DocumentoCiudadanoSerializer
  

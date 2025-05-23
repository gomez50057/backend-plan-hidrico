from django.urls import path
from . import views

app_name = 'ecos_ciudadania'

urlpatterns = [
    path('ecos-ciudadania/documentos/', views.DocumentoListCreateAPIView.as_view(), name='api_lista_crear_documentos'),
    path('ecos-ciudadania/documentos/<int:pk>/', views.DocumentoDetailAPIView.as_view(), name='api_detalle_documento'),
]

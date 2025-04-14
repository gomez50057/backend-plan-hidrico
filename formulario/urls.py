# formulario/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NivelacionTierraViewSet, ArchivoPDFViewSet

router = DefaultRouter()
router.register('formularios', NivelacionTierraViewSet)
router.register('archivos', ArchivoPDFViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

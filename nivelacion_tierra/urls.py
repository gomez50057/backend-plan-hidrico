# nivelacion_tierra/urls.py
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('formulario.urls')),
    path('api/', include('auth_app.urls')),
    path('api/', include('ecos_ciudadania.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# nivelacion_tierra/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('formulario.urls')),
    path('api/', include('auth_app.urls')),

]

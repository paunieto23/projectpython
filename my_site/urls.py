"""
urls.py

Defineix les rutes principals del projecte Django 'my_site'.

Inclou:
- Ruta per al panell d'administració.
- Inclusió de les rutes de l'aplicació 'concesionario'.
- Servei d’arxius multimèdia en mode desenvolupament.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Panell d’administració de Django
    path('', include('concesionario.urls')),  # Rutes de l'aplicació principal
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Servei d’arxius multimèdia durant el desenvolupament

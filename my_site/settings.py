"""
settings.py

Configuració principal del projecte Django 'my_site'.

Inclou:
- Configuració de seguretat i entorn.
- Llista d'aplicacions instal·lades i middlewares.
- Rutes, plantilles, base de dades i autenticació.
- Configuració d'idioma, fus horari i arxius estàtics i multimèdia.
"""

import os
from pathlib import Path

# Directori base del projecte
BASE_DIR = Path(__file__).resolve().parent.parent

# Clau secreta per a l'aplicació (canvia-la en producció!)
SECRET_KEY = 'django-insecure-replace-this-with-a-secure-key'

# Activa el mode debug (només en desenvolupament)
DEBUG = True

# Llista d’hostings permesos (deixa-ho buit en desenvolupament)
ALLOWED_HOSTS = []

# Aplicacions instal·lades
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'concesionario',  # Aplicació pròpia
]

# Middleware utilitzat pel projecte
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arxiu de rutes principal
ROOT_URLCONF = 'my_site.urls'

# Configuració dels templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta personalitzada de plantilles
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuració WSGI/ASGI
WSGI_APPLICATION = 'my_site.wsgi.application'
ASGI_APPLICATION = 'my_site.asgi.application'

# Configuració de la base de dades (SQLite per defecte)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validació de contrasenyes
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuració de l’idioma i zona horària
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuració d’arxius estàtics i multimèdia
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

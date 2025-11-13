from pathlib import Path
import os  # ← Agregado para rutas

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-rnmkyu=7#ne!p(h$l7%eip9*h&mtv(s^l&rco+r0=9f(5o8t_u'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'liberacion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'liberacion_ingles_XM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'liberacion', 'templates')],  # ← Ruta de plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'liberacion_ingles_XM.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-mx'  # ← Español para México
TIME_ZONE = 'America/Mexico_City'  # ← Zona horaria local
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'liberacion', 'static')]  # ← Ruta de archivos estáticos

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirecciones de login/logout
LOGIN_URL = '/login/'               # ← Obligatorio para que @login_required funcione
LOGIN_REDIRECT_URL = '/redirigir/'  # ← Después de login, redirige según el rol
LOGOUT_REDIRECT_URL = '/login/'     # ← Después de logout, regresa al login

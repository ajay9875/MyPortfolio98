import os
from pathlib import Path
from decouple import config

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=True, cast=bool)

# Hosts configuration
BASE_ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', 'myportfolio24*7.onrender.com']
env_hosts = config("ALLOWED_HOSTS", default='').split(',')

ALLOWED_HOSTS = [host.strip() for host in BASE_ALLOWED_HOSTS + env_hosts if host.strip()]

# Application definition
INSTALLED_APPS = [
    'Myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Only for dev
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Myproject.wsgi.application'

# Database (using SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # for collectstatic
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'Myapp' / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Whitenoise static storage
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    }
}

# Auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Whitenoise settings
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_MAX_AGE = 31536000  # 1 year cache

# HTTPS and Cookie Security
if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Add this import if not already present at top
import os

# Add these MEDIA settings only if they don't exist
if not hasattr(globals(), 'MEDIA_URL'):
    MEDIA_URL = '/media/'
if not hasattr(globals(), 'MEDIA_ROOT'):
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Add to STATICFILES_DIRS only if it exists but doesn't contain your static path
if 'STATICFILES_DIRS' in globals():
    static_path = os.path.join(BASE_DIR, 'static')
    if static_path not in STATICFILES_DIRS:
        STATICFILES_DIRS.append(static_path)
else:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Add these file upload settings only if they don't exist
if not hasattr(globals(), 'FILE_UPLOAD_MAX_MEMORY_SIZE'):
    FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB
if not hasattr(globals(), 'DATA_UPLOAD_MAX_MEMORY_SIZE'):
    DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB

# Add X-Frame-Options only if not set
if not hasattr(globals(), 'X_FRAME_OPTIONS'):
    X_FRAME_OPTIONS = 'SAMEORIGIN'

import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
    },
}

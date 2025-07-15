import os
from pathlib import Path
from decouple import config

# BASE_DIR using pathlib (recommended in Django >=3.1)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
#ALLOWED_HOSTS = []
# Base allowed hosts (development defaults)
BASE_ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# Environment variable hosts (production)
ENV_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Combine both lists and filter empty strings
ALLOWED_HOSTS = [host for host in [*BASE_ALLOWED_HOSTS, *ENV_HOSTS] if host]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Myapp',  # Your custom app
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Myproject.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Place your static files here
]

# Manualy Imported
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# KEEP ONLY ONE COPY OF THESE (remove duplicates):
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collectstatic
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Your source files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Consistent 30-minute (1800s) timeout
SESSION_COOKIE_AGE = 1800  # 30 minutes in seconds
SESSION_SAVE_EVERY_REQUEST = True  # Renew timer on activity
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Use persistent sessions

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Serve media files in development
if DEBUG:
    from django.conf.urls.static import static
    MEDIAFILES = static(MEDIA_URL, document_root=MEDIA_ROOT)
else:
    MEDIAFILES = []

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Whitenoise compression and caching
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_MAX_AGE = 31536000  # 1 year cache

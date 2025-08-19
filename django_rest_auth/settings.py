from pathlib import Path
from datetime import timedelta
import os
import dj_database_url
from dotenv import load_dotenv

# -----------------------------
# Chemin de base du projet
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Charger le fichier .env
# -----------------------------
load_dotenv(BASE_DIR / ".env")

# -----------------------------
# Paramètres de sécurité
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "quickhelpapi.onrender.com",  
    "127.0.0.1",                  
    "localhost",                  
]


# -----------------------------
# Applications installées
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'backend',
    'social_accounts',
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'cloudinary',
    'cloudinary_storage',
]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [ "http://localhost:5173", 
                        "https://quickhelpapi.onrender.com"]

ROOT_URLCONF = 'django_rest_auth.urls'

# -----------------------------
# Templates
# -----------------------------
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

WSGI_APPLICATION = 'django_rest_auth.wsgi.application'

AUTH_USER_MODEL = "accounts.User"

# -----------------------------
# Base de données
# -----------------------------
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://admin_rwc5_user:dfVAe5J43iFMbGzU8VHJckyVm2ZAhWxN@dpg-d28rhchr0fns73eo743g-a.oregon-postgres.render.com/admin_rwc5'
    )
}
# -----------------------------
# REST Framework
# -----------------------------
REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# -----------------------------
# Social auth
# -----------------------------
DOMAIN = 'http://localhost:5173'
SITE_NAME = 'django_rest_auth'

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_SECRET = os.getenv("GITHUB_SECRET")
SOCIAL_AUTH_PASSWORD = "jgk348030gjw03"

# -----------------------------
# Password validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -----------------------------
# Internationalisation
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Fichiers statiques et médias
# -----------------------------
STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dodgzhy3g',
    'API_KEY': '171366167264653',
    'API_SECRET': 'liPtsV08cRvm-BUxUY_Qef2aUQc'
}

# -----------------------------
# Email
# -----------------------------
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'ahiaboremmanuel9@gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 2525

# -----------------------------
# Clé par défaut pour les modèles
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

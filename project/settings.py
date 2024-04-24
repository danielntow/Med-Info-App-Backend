"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
from datetime import timedelta

import dotenv

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ALLOWED_ORIGINS = [
    "https://med-info-apps.up.railway.app",
    "https://6623acaa1dda68bf30c2c421--gregarious-tartufo-444727.netlify.app",
    "https://jocular-kashata-e2b6a1.netlify.app",
    "https://main--gregarious-tartufo-444727.netlify.app",
    "https://jocular-kashata-e2b6a1.netlify.app",
    "http://localhost:5173",
    "https://med-info-app.up.railway.app",
]


# ALLOWED_HOSTS = [
#     "http://localhost:8000",
#     "http://localhost:5001",
#     "http://localhost:3000",
#     "http://localhost:5173",
#     "http://127.0.0.1:8000",
#     "http://localhost:5173",
#     "https://med-info-app.up.railway.app",
#     '127.0.0.1',
#     'localhost'
# ]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "myusers.apps.MyusersConfig",
    "medinfo.apps.MedinfoConfig",
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "rest_framework.authtoken",
    "djoser",
    "rest_framework_swagger",
    # "django.contrib.staticfiles",  # required for serving swagger ui's css/js files
    "drf_yasg",
]

AUTH_USER_MODEL = "myusers.NewUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "project/templates",
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.environ.get("DATABASE_NAME"),
#         "USER": "postgres",
#         "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
#         "HOST": os.environ.get("DATABASE_HOST"),
#         "PORT": 20512,
#     }
# }


# DATABASES = {
#     "default": {
#         "ENGINE": 'django.db.backends.mysql',
#         "NAME": os.environ.get("DATABASE_NAME"),
#         "USER": os.environ.get("DATABASE_USERNAME"),
#         "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
#         "HOST": os.environ.get("DATABASE_HOST"),
#         "PORT": os.environ.get("DATABASE_PORT"),
#     }
# }


# settings.py

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'railway',
#         'USER': 'root',
#         'PASSWORD': os.environ.get('MY_PASSWORD'),
#         'HOST': 'viaduct.proxy.rlwy.net',  # or '127.0.0.1' for local development
#         'PORT': '16280',  # MySQL default port
#     }
# }

# settings.py

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'KNtXCBPvNJyTvnHdeSirtGAxJNVtuuxY',
#         # or the IP address or hostname of your PostgreSQL server
#         'HOST': 'roundhouse.proxy.rlwy.net',
#         'PORT': '5432',       # default PostgreSQL port
#     }
# }


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "postgres",  # Maintenance database
#         "USER": "postgres",
#         # Ensure this is set in your environment
#         "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
#         "HOST": "roundhouse.proxy.rlwy.net",
#         "PORT": 20512,
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")
MEDIA_URL = "/media/"


FILE_UPLOAD_PERMISSIONS = 0o640

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        # 'api.authentication.TokenAuthentication'
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "PAGE_SIZE": 100,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

COMPRESS_ROOT = BASE_DIR / "static"

COMPRESS_ENABLED = True


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=300),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # rotate - keeps login after the expiratuon of refresh-token iof user persist
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

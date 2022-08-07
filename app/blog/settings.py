import os
from pathlib import Path

from dotenv import load_dotenv

ENV=os.environ.get('ENV', default='dev')

if ENV=='dev':
    env_file='../.env.dev'
elif ENV=='prod':
    env_file='../.env.prod'
elif ENV=='test':
    env_file='../.env.test'
elif ENV=='stagging':
    env_file='../.env.stagging'
    
if env_file:
    load_dotenv(dotenv_path=env_file)
else:
    load_dotenv(dotenv_path='../.env')

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = str(os.getenv('DJANGO_SECRET_KEY'))
DEBUG = bool(os.getenv('DJANGO_DEBUG'))
hosts = str(os.getenv('DJANGO_ALLOWED_HOSTS'))
if hosts:
    ALLOWED_HOSTS = hosts.split(',')

# setting up https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',    
    'home',
    'article',
    'user',
    'mail',
    'factory',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'mediafiles/generated_templates')],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": str(os.getenv("SQL_ENGINE", "django.db.backends.sqlite3")),
        "NAME": str(os.getenv("SQL_DATABASE", BASE_DIR / "db.sqlite3")),
        "USER": str(os.getenv("SQL_USER", "django")),
        "PASSWORD": str(os.getenv("SQL_PASSWORD", "django")),
        "HOST": str(os.getenv("SQL_HOST", "localhost")),
        "PORT": str(os.getenv("SQL_PORT", "5432")),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Indian/Reunion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
MEDIA_URL = "/media/"
LOGIN_REDIRECT_URL="home"
LOGOUT_REDIRECT_URL="home"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TESTS_SHOW_BROWSER = True
# django allauth registration settings
AUTH_USER_MODEL = 'user.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID=1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_FORMS = {
    'login': 'user.forms.CustomLoginForm',
    'signup': 'user.forms.RegisterForm'
}

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.hostinger.com"
EMAIL_PORT = 465
EMAIL_HOST_USER= str(os.getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD= str(os.getenv('EMAIL_HOST_PASSWORD'))
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL='blog@slb-fullweb.tech'



# raven settings

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]

RAVEN_CONFIG = {
    'dsn': 'https://dfe6351a70a444b3a57edb8901ce1adb@o1259826.ingest.sentry.io/6435066' # caution replace by your own!!
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO', # WARNING by default. Change this to capture more than warnings.
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

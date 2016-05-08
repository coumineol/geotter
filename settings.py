
import os
from unipath import Path
import dj_database_url


BASE_DIR = Path(__file__).ancestor(1)


f = open('note.txt')
SECRET_KEY = f.read().strip()
f.close()

DEBUG = False

if DEBUG == True:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['deneme123123.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lctst.apps.app1',
    'lctst.apps.app2',
    'celery',
    'unipath',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lctst.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'lctst.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dc7fhahcqdl4pb',
        'USER': 'goycrtmxfwfwhs',
        'PASSWORD': '',
        'HOST': 'ec2-54-204-41-46.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_PATH = os.path.join(BASE_DIR, 'static') + '/'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot') + '/'

STATICFILES_DIRS = (
    STATIC_PATH,
)


# BROKER_URL = 'redis://localhost:6379'
BROKER_URL = 'redis://lctst:ogre8891@pub-redis-10055.us-east-1-2.5.ec2.garantiadata.com:10055'

CELERY_RESULT_BACKEND = 'redis'

CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Africa/Nairobi'

BROKER_POOL_LIMIT = 2
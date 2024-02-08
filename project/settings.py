import os
from environs import Env
from pathlib import Path


env = Env()
env.read_env()



DATABASES = {
    'default': {
        'DB_ENGINE': env('DB_ENGINE'),
        'DB_HOST': env('DB_HOST'),
        'DB_PORT': env('DB_PORT'),
        'DB_NAME': env('DB_NAME'),
        'DB_USER': env('DB_USER'),
        'DB_PASSWORD': env('DB_PASSWORD'),
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool("DEBUG")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

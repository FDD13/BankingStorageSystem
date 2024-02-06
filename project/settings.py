import os
from environs import Env
from pathlib import Path

env = Env()
env.read_env()


engine = env('ENGINE')
host = env('HOST')
port = env.int('PORT')
name = env('NAME')
user = env('USER')
password = env('PASSWORD')


DATABASES = {
    'default': {
        'ENGINE': engine,
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool("DEBUG")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']



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

from .base import *
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'ithilleldb'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', '123'),
            'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'ATOMIC_REQUESTS': True
    }
}

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-kima)d7o_%ip)!%3^c%-b=pb&-j1(au9*ep@8(0y-(j-jw73ec')


MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'


EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'aws-smtp.us-east-1.amazonaws.com')
EMAIL_PORT = os.getenv('EMAIL_PORT', '465')
EMAIL_USE_TLS = str(os.getenv('EMAIL_USE_TLS')).lower() in ('true', '1')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'

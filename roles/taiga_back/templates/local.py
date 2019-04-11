from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "{{ postgresql_db_name }}",
        'USER': "{{ postgresql_user_name }}",
        'PASSWORD': "{{ postgresql_user_password }}",
        'HOST': '',
        'PORT': '',
    }
}

SITES = {
    "api": {
       "scheme": "http",
       "domain": "{{ taiga_server_ip }}:80",
       "name": "api"
    },
    "front": {
       "scheme": "http",
       "domain": "{{ taiga_server_ip }}:9001",
       "name": "front"
    },
}

SITE_ID = "api"

MEDIA_ROOT = '/home/taiga/taiga-back-stable/media'
STATIC_ROOT = '/home/taiga/taiga-back-stable/static'

MEDIA_URL = "http://{{ taiga_server_ip }}/media/"
STATIC_URL = "http://{{ taiga_server_ip }}/static/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "{{ taiga_server_ip }}"

TIME_ZONE = "Asia/Shanghai"
USE_TZ = False

LANGUAGE_CODE = 'zh-hans'

#SECRET_KEY = "theveryultratopsecretkey"
SECRET_KEY = "{{ taiga_secret_key }}"

DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@{{ taiga_server_ip }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:taiga123@localhost:5672/taiga"}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"

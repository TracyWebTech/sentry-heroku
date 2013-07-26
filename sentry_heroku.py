import os

import dj_database_url
from sentry.conf.server import *


DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost')
}

SENTRY_KEY = str(DATABASES['default'])

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ['PORT']
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'worker_class': 'gevent'
}

SENTRY_ALLOW_REGISTRATION = False


DEFAULT_FROM_EMAIL = 'Tracy Logging Service <noreply@tracy.com.br>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sendmail@tracy.com.br'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587

for env_key, env_value in os.environ.iteritems():
    if env_key.startswith('SENTRY_'):
        globals()[env_key] = env_value

from base import *
import dj_database_url
import os

"""REMEMBER TO SET DEBUG TO OFF WHEN IT WORKS WELL ON PRODUCTION"""
DEBUG = True

TEMPLATE_DEBUG = True

# Parse database configuration from $DATABASE_URL

DATABASES = {'default': dj_database_url.config() }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


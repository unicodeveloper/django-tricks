# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import envvars
envvars.load()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = envvars.get('SECRET_KEY')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'tricks'
)

# Authentication backends Setting
AUTHENTICATION_BACKENDS = (
# For Facebook Authentication
'social.backends.facebook.FacebookOAuth2',

# For github Authentication
'social.backends.github.GithubOAuth2',

# For Twitter Authentication
'social.backends.twitter.TwitterOAuth',

# For Google Authentication
'social.backends.google.GoogleOpenId',
'social.backends.google.GoogleOAuth2',
'social.backends.google.GoogleOAuth',

# Default Django Auth Backends
'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'tricks.Profile'

REDIRECT_URIs = ["http://localhost:8000/complete/google-oauth2/","http://127.0.0.1:8000/complete/twitter/","http://127.0.0.1:8000/complete/google-oauth2/", "http://django-tricks.herokuapp.com/complete/google-oauth2/"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = envvars.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = envvars.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')

# Twitter Auth Details
SOCIAL_AUTH_TWITTER_SECRET = envvars.get('SOCIAL_AUTH_TWITTER_SECRET')
SOCIAL_AUTH_TWITTER_KEY = envvars.get('SOCIAL_AUTH_TWITTER_KEY')

# Github Auth Details
SOCIAL_AUTH_GITHUB_KEY = envvars.get('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = envvars.get('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = envvars.get('SOCIAL_AUTH_LOGIN_REDIRECT_URL')
SOCIAL_AUTH_LOGIN_ERROR_URL = envvars.get('SOCIAL_AUTH_LOGIN_ERROR_URL')



SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'tricks.pipeline.get_profile_picture'
)


TEMPLATE_CONTEXT_PROCESSORS = (
    # Default Template context processors
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    # Setting of Template Context Processors for Social Auth
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django-tricks.urls'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR +'/templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'django-tricks.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


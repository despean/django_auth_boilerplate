"""
Django settings for account project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cqwfsl!+q55li=wt36b28bh292n&(u1c=#()f(x47k19sld=(m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'sorl.thumbnail',
  'authaccount',
  'social_django',

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

ROOT_URLCONF = 'account.urls'

# AUTH_USER_MODEL = 'account.User'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'images/templates')],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'social_django.context_processors.backends',
        'social_django.context_processors.login_redirect',
      ],
      'libraries': {
        'app_tags': 'authaccount.templatetags.app_tags',

      }
    },
  },
]

WSGI_APPLICATION = 'account.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
  }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# authentication backends
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'authaccount.authentication.EmailAuthBackend',
  'social_core.backends.twitter.TwitterOAuth',
  'social_core.backends.facebook.FacebookOAuth2',
  # 'social_core.backends.google.GoogleOpenId',
  'social_core.backends.google.GoogleOAuth2',
  'social_core.backends.google.GoogleOAuth',
)

# social auth
SOCIAL_AUTH_FACEBOOK_KEY = '553325091721801'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'a50329b247f7dfcccef0a0676010b6f3'  # Facebook App Secret

SOCIAL_AUTH_TWITTER_KEY = 'mdI4jjBi4DDgTt7kAgxaUcrj7'
SOCIAL_AUTH_TWITTER_SECRET = 'H7gjPFbxltg52APJpvZ0mRJa8fwEVwGjtPdq7j3DZ2N62aqB5y'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1002620928133-lsnoqbpsja5c8g6obmtqhp41bvv9svv0.apps.googleusercontent.com'  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xY9MJ-TIPGaf0MpImcfVdCEQ'  # Google Consumer Secret
GOOGLE_WHITE_LISTED_DOMAINS = ['django.com:8000']

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', ]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'name,first_name,last_name,birthday'
}
FACEBOOK_EXTENDED_PERMISSIONS = ['user_birthday']
# SOCIAL_AUTH_TWITTER_SCOPE = ['email']

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_PIPELINE = (
  'social_core.pipeline.social_auth.social_details',
  'social_core.pipeline.social_auth.social_uid',
  'social_core.pipeline.social_auth.social_user',
  'social_core.pipeline.user.get_username',
  'social_core.pipeline.user.create_user',
  'social_core.pipeline.social_auth.associate_user',
  'social_core.pipeline.social_auth.load_extra_data',
  'social_core.pipeline.user.user_details',
  'social_core.pipeline.social_auth.associate_by_email',
  'authaccount.pipeline.get_profile_picture'
)

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Douala'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles'),

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "authaccount/static"),
]
# django auth settings
from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('account:dashboard')
LOGIN_URL = reverse_lazy('account:login')
LOGOUT_URL = reverse_lazy('account:logout')
LOGOUT_REDIRECT_URL = reverse_lazy('account:login')

# email backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djangoappmail@gmail.com'
EMAIL_HOST_PASSWORD = 'stdjango'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# media setup
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# TEMPLATE_DEBUG = True
# get absolute url
ABSOLUTE_URL_OVERRIDES = {
  'auth.user': lambda u: reverse_lazy('account:user_detail', args=[u.username])
}

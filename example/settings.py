"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

# Application definition

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

PROJECT_APPS = [
    'django_su',
    'django.contrib.admin',
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',

    'formadmin',  # pip install django-form-admin
    'ajax_select',  # pip install django-ajax-select
] + PROJECT_APPS


ROOT_URLCONF = 'example.urls'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "django_su.backends.SuBackend",
)

# URL to redirect after the login.
# Default: "/"
SU_LOGIN_REDIRECT_URL = "/" 

# URL to redirect after the logout.
# Default: "/"
SU_LOGOUT_REDIRECT_URL = "/"

# A function to specify the perms that the user must have can use django_su
# Default: None
SU_LOGIN_CALLBACK = "example.utils.su_login_callback"

# A function to override the django.contrib.auth.login(request, user)
# function so you can set session data, etc.
# Default: None
SU_CUSTOM_LOGIN_ACTION = "example.utils.custom_login"

if 'ajax_select' in INSTALLED_APPS:
    AJAX_LOOKUP_CHANNELS = {
        'django_su':  dict(model='auth.user', search_field='username'),
    }

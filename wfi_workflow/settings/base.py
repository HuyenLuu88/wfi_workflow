"""
Django settings for wfi_workflow project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ
from decouple import Csv, Config, RepositoryEnv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Add .env.dev variables anywhere before SECRET_KEY
# dotenv_file = os.path.join(BASE_DIR, ".env.dev")
# if os.path.isfile(dotenv_file):
#     dotenv.load_dotenv(dotenv_file)



env = environ.Env()
# reading .env.dev file
#environ.Env.read_env()

if os.environ['DJANGO_SETTINGS_MODULE'] == 'wfi_workflow.settings.prod':
    DOTENV_FILE = '.env.prod'
    config = Config(RepositoryEnv(DOTENV_FILE)).get

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

else:

    DOTENV_FILE = '.env.dev'
    config = Config(RepositoryEnv(DOTENV_FILE)).get

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

#print(BASE_DIR)




# Application definition

INSTALLED_APPS = [
    'captcha',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.portfolio',
    'apps.product',
    'apps.task',
    'django_bootstrap_breadcrumbs',
    #'axes',
    #2fa
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    'widget_tweaks',
    'crispy_forms',
    'django_countries',
    'smart_selects',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #2fa
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wfi_workflow.middleware.LoginRequiredMiddleware',
    #'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'wfi_workflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
# TEST_DIR = Path(__file__).resolve().parent.parent
# print(os.path.join(TEST_DIR, 'templates'))
#
# TEST_DIR = Path(__file__).resolve().parent.parent.parent
# print(os.path.join(TEST_DIR, 'templates'))


WSGI_APPLICATION = 'wfi_workflow.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [ os.path.join(BASE_DIR,'static') ]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')


AUTH_EXEMPT_ROUTES = ('register', 'login', 'request-password', 'reset-user-password', 'verify_email', 'activate_account', 'account', 'test2', 'account')
AUTH_LOGIN_ROUTE = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

RECAPTCHA_REQUIRED_SCORE = 0.85

# AUTHENTICATION_BACKENDS = [
#     'axes.backends.AxesBackend',
# ]


# AXES_LOCK_OUT_AT_FAILURE = False
# AXES_RESET_ON_SUCCESS=True

#2fa
LOGIN_URL = 'two_factor:login'

LOGIN_REDIRECT_URL = 'home'

USE_DJANGO_JQUERY = True

DATE_FORMAT = '%m/%d/%Y'
DATETIME_FORMAT = '%m/%d/%Y %I:%M'

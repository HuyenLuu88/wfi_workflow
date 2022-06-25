from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# Debug mode
DEBUG = config('DEBUG', cast=bool)

# Allowed hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Protcol used for the domain
DOMAIN_PROTOCOL = config("DOMAIN_PROTOCOL")

# SECURITY WARNING: keep the secret key used in production secret!
# Django Project Secret Key
SECRET_KEY = config("SECRET_KEY")

# Google ReCaptcha Public/Private Keys
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')

# Database Config/Credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', cast=int),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
    }
}

# SMTP Configuration
# MAIL_ADMIN = 'youcef_laifa@hotmail.com'
EMAIL_FROM_USER = config('EMAIL_FROM_USER')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Users logged in session will auto logout after SESSION_COOKIE_AGE
SESSION_COOKIE_AGE = config('SESSION_COOKIE_AGE', cast=int)

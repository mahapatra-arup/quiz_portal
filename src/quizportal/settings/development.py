#ref :https://simpleisbetterthancomplex.com/tips/2017/07/03/django-tip-20-working-with-multiple-settings-modules.html
#import setting
from .base import *
# from .tinymce_settings import *
# from .django_jet_settings import *

#messgage :Bootstrap Snippet
from django.contrib import messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# gives the root of the project: root/. This is THE ROOT OF THE PROJECT.
PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__name__))

INSTALLED_APPS += [
     #3rd prty
    # 'simple_pagination',
    # 'tinymce',
    # All your other apps here
    # 'mptt',

    #My app
    'quiz',
    'users',
    'core',

    #SHOP
    'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'crispy_forms',
    # 'django_countries',

]

#for User AbstractUser field add:
AUTH_USER_MODEL = 'users.User'

#for django.contrib.site
SITE_ID = 1

#For crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Allauth ----------
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend'
# )



# after login redirect to
# LOGIN_REDIRECT_URL = '/'

#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#install :- https://pypi.org/project/psycopg2/
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',#'django.db.backends.postgresql_psycopg2', 
        'NAME':     'quiz',
        'USER':     'postgres',
        'PASSWORD': '!dcuseronly',
        'HOST':     'localhost'
    }
}

# #Heroku DATABASES['default']
# import dj_database_url
# DATABASES =  {'default':dj_database_url.config(default='postgres://xmwffnfspuwngf:f47eaaf1142777a89bec380253fd498c938c38639ee2ddd13c320cfa88a4a6a2@ec2-52-45-14-227.compute-1.amazonaws.com:5432/d9k5asqgavu083')}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


#Email Details

EMAIL_HOST = 'mail.pytube.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@pytube.net'
EMAIL_HOST_PASSWORD = 'A8001854806m@'
EMAIL_USE_TLS = True
# Set EMAIL_BACKEND to 'django.core.mail.backends.smtp.EmailBackend'
# in production
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# SENDER_EMAIL, REPLY_EMAIL, PRODUCTION_URLare used in email

# This email id will be used as <from address> for sending emails.
# For example no_reply@<your_organization>.in can be used.
SENDER_EMAIL = 'info@pytube.net'

# Organisation/Indivudual Name.
SENDER_NAME = 'pytube'

# This email id will be used by users to send their queries
# For example queries@<your_organization>.in can be used.
REPLY_EMAIL = 'info@pytube.net'

# This url will be used in email verification to create activation link.
# Add your hosted url to this variable.
# For example https://127.0.0.1:8000 or 127.0.0.1:8000
PRODUCTION_URL = 'pytube.net'


#blog sign
PORTAL_AUTHOR = "Online Quiz Portal | Arup Mahapatra"




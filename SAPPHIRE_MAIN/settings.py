
import os
from pathlib import Path

from pickle import FALSE, TRUE
from socket import if_nameindex

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7hljt!*b3j*)g%o5zt+ql!3mg$q$xk(ocd=_ex5a1atx-!$)@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG == False:
    ALLOWED_HOSTS = ['www.sapphirecommotrade.com','sapphirecommotrade.com','localhost']
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',
    'storages',
    #'admin_honeypot',
    
    'Sapphire.apps.SapphireConfig',
    
    'django.contrib.sitemaps'

]
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
]

ROOT_URLCONF = 'SAPPHIRE_MAIN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Sapphire.context_processors.Sapphire_Settings', #user define context processor
                'Sapphire.context_processors.Sapphire_About_us',
                'Sapphire.context_processors.Sapphire_Home_image',
                'Sapphire.context_processors.Sapphire_Product2',
                'Sapphire.context_processors.Sapphire_contactus',
                'Sapphire.context_processors.Sapphire_Product1',
                'Sapphire.context_processors.Sapphire_EndSectionOfProduct',
             
            
            ],
        },
    },
]

WSGI_APPLICATION = 'SAPPHIRE_MAIN.wsgi.application'

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdhaM4hAAAAALK9M-GFJu1ZE75JB696ifh28ROe'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'sapphire_main',
            'USER' : 'nitensapkota1705',
            'PASSWORD' : 'nitensapkota10101111',
            'HOST' : 'localhost',
            'PORT' : '',
    }
    }
else:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'Sapphire_Main',
            'USER' : 'nitensapkota1705',
            'PASSWORD' : 'nitensapkota10101111',
            'HOST' : 'database-1.cffz4bxhc8ow.us-east-1.rds.amazonaws.com',
            'PORT' : '5432',
    }
    }


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


if DEBUG == False:
    STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
    ]

    AWS_ACCESS_KEY_ID = "3RWENTXA6CAUUYKFTV7O"
    AWS_SECRET_ACCESS_KEY = "aVwwmmEcR2XUccrORbzCD/GsR8hQoEhEhtsWJre/Rg4" 
    AWS_STORAGE_BUCKET_NAME = "open-sapphiremain-spaces"
    AWS3_S3_OBJECT_PARAMETERS = {
        'CacheControl' : 'max-age=86400',
    } 

    AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
    AWS_S3_CUSTOM_DOMAIN = 'static.sapphirecommotrade.com'
    AWS_LOCATION = 'open-sapphiremain-spaces'
    AWS_DEFAULT_ACL = 'public-read'

    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




    STATIC_URL = '{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)


else:

    STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
    ]

    STATIC_URL = '/static/'

    MEDIA_URL = '/images/'



    MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sapphire.upvc@gmail.com'
EMAIL_HOST_PASSWORD = 'hxtbiphpaifiibob'
#EMAIL_USE_SSL = True
EMAIL_USE_TLS = True








JAZZMIN_SETTINGS = {
    "site_title": "Sapphire",
    "site_header": "Sapphire",
    "site_brand": "Sapphire",
    "site_icon": 'images/SAPPHIRE_COMMOTRADE_FINAL_Logo_2.png',
    # Add your own branding here
    "site_logo": 'images/SAPPHIRE_COMMOTRADE_FINAL_Logo_2.png',
    "welcome_sign": "Welcome to the Sapphire",
    # Copyright on the footer
    "copyright": "Sapphire",
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
 
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    
    "icons": {
        "auth": "fas fa-users-cog",
       "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    
    # # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    # Uncomment this line once you create the bootstrap-dark.css file
    # "custom_css": "css/bootstrap-dark.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cyborg",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

#coding=utf-8
import os
import sys

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'extern'))
#====================================================================================
#                  A D M I N I S T R A T I O N  &  S E C UR I T Y
#====================================================================================
SITE_ID = 1
SECRET_KEY = ''
ADMINS = ()
MANAGERS = ()
INTERNAL_IPS = ()
SEND_BROKEN_LINK_EMAILS = False
#====================================================================================
#                                   D E B U G
#====================================================================================
DEBUG = False
TEMPLATE_DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False
#====================================================================================
#                               D A T A B A S E S 
#====================================================================================
DATABASES = {}
DATABASE_ROUTERS = []
DEFAULT_TABLESPACE = ''
DEFAULT_INDEX_TABLESPACE = ''
#====================================================================================
#                                   T E S T S 
#====================================================================================
TEST_RUNNER = ''
FIXTURE_DIRS = ''
#====================================================================================
#                                   C A C H E
#====================================================================================
CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
#====================================================================================
#                                S E S S I O N S
#====================================================================================
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SECURE = False
SESSION_DB_ALIAS = None
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_FILE_PATH = None
SESSION_SAVE_EVERY_REQUEST = False
#====================================================================================
#                                  E M A I L
#====================================================================================
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = 'marat@localhost'
EMAIL_FILE_PATH = None
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = '[Django] '
EMAIL_USE_TLS = False
#====================================================================================
#                        T I M E Z O N E  &  L O C A L E S
#====================================================================================
USE_I18N = True
LOCALE_PATHS = ()
LANGUAGE_CODE = 'ru-RU'
LANGUAGES = (
             ('ru', 'Russian')
            )
LANGUAGE_COOKIE_NAME = 'django_language'
USE_L10N = True
TIME_ZONE = 'Europe/Moscow'
FIRST_DAY_OF_WEEK = 1
DECIMAL_SEPARATOR = '.'
USE_THOUSAND_SEPARATOR = True
NUMBER_GROUPING = 3
THOUSAND_SEPARATOR = ' '
#====================================================================================
#                         D A T E T I M E   F O R M A T S
#====================================================================================
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y, H:i:s'
TIME_FORMAT = 'H:i'
SHORT_DATE_FORMAT = 'd.m.Y'
SHORT_DATETIME_FORMAT = 'd.m.Y, H:i'
MONTH_DAY_FORMAT = 'j F'
YEAR_MONTH_FORMAT = 'F Y'
DATE_INPUT_FORMATS = ('%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y',)
TIME_INPUT_FORMATS = ('%H:%M', '%H:%M:%S',)
DATETIME_INPUT_FORMATS = ('%d.%m.%Y %H:%M', '%d/%m/%Y %H:%M', '%d-%m-%Y %H:%M',
                          '%d.%m.%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', '%d-%m-%Y %H:%M:%S',
                          '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y',
                          )
FORMAT_MODULE_PATH = None
#====================================================================================
#                      M E D I A   P A T C H E S   &  U R L S 
#====================================================================================
MEDIA_ROOT = ''
ALLOWED_INCLUDE_ROOTS = ()
PREPEND_WWW = False
APPEND_SLASH = True
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
IGNORABLE_404_ENDS = ('mail.pl', 'mailform.pl', 'mail.cgi', 'mailform.cgi', 'favicon.ico', '.php')
IGNORABLE_404_STARTS = ('/cgi-bin/', '/_vti_bin', '/_vti_inf')
ABSOLUTE_URL_OVERRIDES = {}
#====================================================================================
#                        R E Q U E S T  &   R E S P O N S E
#====================================================================================
FORCE_SCRIPT_NAME = None
DISALLOWED_USER_AGENTS = ()
from django import get_version
URL_VALIDATOR_USER_AGENT = "Django/%s (http://www.djangoproject.com)" % get_version()
DEFAULT_CHARSET = 'utf-8'
DEFAULT_CONTENT_TYPE = 'text/html'
USE_ETAGS = False
#====================================================================================
#                                L O A D E R S
#====================================================================================
FILE_CHARSET = 'utf-8'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
                        "django.core.files.uploadhandler.TemporaryFileUploadHandler",)
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
FILE_UPLOAD_TEMP_DIR = None
FILE_UPLOAD_PERMISSIONS = None
#====================================================================================
#                            A U T H E N I C A T I O N
#====================================================================================
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
AUTH_PROFILE_MODULE = None
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/accounts/profile/'
PASSWORD_RESET_TIMEOUT_DAYS = 3
#====================================================================================
#                                T E M P L A T E S
#====================================================================================
TEMPLATE_CONTEXT_PROCESSORS = ( "django.core.context_processors.auth",
                                "django.core.context_processors.debug",
                                "django.core.context_processors.i18n",
                                "django.core.context_processors.media",
                                "django.contrib.messages.context_processors.messages")
TEMPLATE_DIRS = ()
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader')
TEMPLATE_STRING_IF_INVALID = ''
#====================================================================================
#                  M I D D L E W A R E S  &  A P P L I C A T I O N S  
#====================================================================================
MIDDLEWARE_CLASSES = (  'django.middleware.common.CommonMiddleware',
                        'django.contrib.sessions.middleware.SessionMiddleware',
                        'django.middleware.csrf.CsrfViewMiddleware',
                        'django.contrib.auth.middleware.AuthenticationMiddleware',
                        'django.contrib.messages.middleware.MessageMiddleware',)
INSTALLED_APPS = (
#                  '',
                 )
ROOT_URLCONF = 'urls'
SERIALIZATION_MODULES = {}
#====================================================================================
#                              M E S S A G I N G  
#====================================================================================
MESSAGE_STORAGE = 'django.contrib.messages.storage.user_messages.LegacyFallbackStorage'
#import django.contrib.messages
#MESSAGE_LEVEL = messages.INFO
#MESSAGE_TAGS = {messages.DEBUG: 'debug',
                #messages.INFO: 'info',
                #messages.SUCCESS: 'success',
                #messages.WARNING: 'warning',
                #messages.ERROR: 'error',}
#====================================================================================
#                                   C S R F 
#====================================================================================
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_DOMAIN = None
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
#====================================================================================
#                                 O T H E R S  
#====================================================================================
ADMIN_FOR = ()
PROFANITIES_LIST = ('asshat', 'asshead', 'asshole', 'cunt', 'fuck', 'gook', 'nigger', 'shit')

from settings_local import *

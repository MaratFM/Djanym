#====================================================================================
#                  A D M I N I S T R A T I O N  &  S E C UR I T Y
#====================================================================================
SITE_ID = 1
SECRET_KEY = 'afa4f437HU^T&GYf8H43J276RDf432&^%RUYrdfUagfu7t3ugfu&ITUYBr9287dO8'
ADMINS = (('Marat', 'maratfm@gmail.com'))
MANAGERS = ADMINS
INTERNAL_IPS = ('127.0.0.1')
SEND_BROKEN_LINK_EMAILS = True
#====================================================================================
#                                   D E B U G
#====================================================================================
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG
#====================================================================================
#                               D A T A B A S E S 
#====================================================================================
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'HOST':     'localhost',
        'USER':     'root',
        'PASSWORD': 'master',
        'NAME':     'default'
    }
}
#====================================================================================
#                                   C A C H E
#====================================================================================
CACHE_BACKEND = 'memcached://localhost:11211/'
CACHE_MIDDLEWARE_KEY_PREFIX = SECRET_KEY+'cache'


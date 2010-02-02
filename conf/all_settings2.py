
ABSOLUTE_URL_OVERRIDES = {}
#Default: {} (Empty dictionary)
#A dictionary mapping "app_label.model_name" strings to functions that take a model object and return its URL. This is a way of overriding get_absolute_url() methods on a per-installation basis. Example:
# ABSOLUTE_URL_OVERRIDES = {
#    'blogs.weblog': lambda o: "/blogs/%s/" % o.slug,
#    'news.story': lambda o: "/stories/%s/%s/" % (o.pub_year, o.slug),
# }
#Note that the model name used in this setting should be all lower-case, regardless of the case of the actual model class name.

ADMIN_FOR = ()
#Default: () (Empty tuple)
#Used for admin-site settings modules, this should be a tuple of settings modules (in the format 'foo.bar.baz') for which this site is an admin.
#The admin site uses this in its automatically-introspected documentation of models, views and template tags.

ADMIN_MEDIA_PREFIX = '/media/'
#Default: '/media/'
#The URL prefix for admin media -- CSS, JavaScript and images used by the Django administrative interface. Make sure to use a trailing slash, and to have this be different from the MEDIA_URL setting (since the same URL cannot be mapped onto two different sets of files).

ADMINS = ()
#Default: () (Empty tuple)
#A tuple that lists people who get code error notifications. When DEBUG=False and a view raises an exception, Django will e-mail these people with the full exception information. Each member of the tuple should be a tuple of (Full name, e-mail address). Example:
# (('John', 'john@example.com'), ('Mary', 'mary@example.com'))
#Note that Django will e-mail all of these people whenever an error happens. See Error reporting via e-mail for more information.

ALLOWED_INCLUDE_ROOTS = ()
#Default: () (Empty tuple)
#A tuple of strings representing allowed prefixes for the {% ssi %} template tag. This is a security measure, so that template authors can't access files that they shouldn't be accessing.
#For example, if ALLOWED_INCLUDE_ROOTS is ('/home/html', '/var/www'), then {% ssi /home/html/foo.txt %} would work, but {% ssi /etc/passwd %} wouldn't.

APPEND_SLASH = True
#Default: True
#Whether to append trailing slashes to URLs. This is only used if CommonMiddleware is installed (see Middleware). See also PREPEND_WWW.

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
#Default: ('django.contrib.auth.backends.ModelBackend',)
#A tuple of authentication backend classes (as strings) to use when attempting to authenticate a user. See the authentication backends documentation for details.

AUTH_PROFILE_MODULE = None
#Default: Not defined
#The site-specific user profile model used by this site. See Storing additional information about users.

CACHE_BACKEND = 'locmem://'
#Default: 'locmem://'
#The cache backend to use. See Django's cache framework.

CACHE_MIDDLEWARE_KEY_PREFIX = ''
#Default: '' (Empty string)
#The cache key prefix that the cache middleware should use. See Django's cache framework.

CACHE_MIDDLEWARE_SECONDS = 600
#Default: 600
#The default number of seconds to cache a page when the caching middleware or cache_page() decorator is used.

CSRF_COOKIE_NAME = 'csrftoken'
#New in Django Development version.
#Default: 'csrftoken'
#The name of the cookie to use for the CSRF authentication token. This can be whatever you want. See Cross Site Request Forgery protection.

CSRF_COOKIE_DOMAIN = None
#New in Django Development version.
#Default: None
#The domain to be used when setting the CSRF cookie. This can be useful for allowing cross-subdomain requests to be exluded from the normal cross site request forgery protection. It should be set to a string such as ".lawrence.com" to allow a POST request from a form on one subdomain to be accepted by accepted by a view served from another subdomain.

CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
#New in Django Development version.
#Default: 'django.views.csrf.csrf_failure'
#A dotted path to the view function to be used when an incoming request is rejected by the CSRF protection. The function should have this signature:
# def csrf_failure(request, reason="")
#where reason is a short message (intended for developers or logging, not for end users) indicating the reason the request was rejected. See Cross Site Request Forgery protection.

DATABASES = {}
#Default: {} (Empty dictionary)
#A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary who's contents maps database aliases to a dictionary containing the options for an individual database.
#The DATABASES setting must configure a default database; any number of additional databases may also be specified.
#The simplest possible settings file is for a single-database setup using SQLite. This can be configured using the following:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase'
#     }
# }
#For other database backends, or more complex SQLite configurations, other options will be required. The following inner options are available.

ENGINE = ''
#Default: '' (Empty string)
#The database backend to use. The built-in database backends are:
#'django.db.backends.postgresql_psycopg2'
#'django.db.backends.postgresql'
#'django.db.backends.mysql'
#'django.db.backends.sqlite3'
#'django.db.backends.oracle'
#You can use a database backend that doesn't ship with Django by setting ENGINE to a fully-qualified path (i.e. mypackage.backends.whatever). Writing a whole new database backend from scratch is left as an exercise to the reader; see the other backends for examples.

HOST = ''
#Default: '' (Empty string)
#Which host to use when connecting to the database. An empty string means localhost. Not used with SQLite.
#If this value starts with a forward slash ('/') and you're using MySQL, MySQL will connect via a Unix socket to the specified socket. For example:
#"HOST": '/var/run/mysql'
#If you're using MySQL and this value doesn't start with a forward slash, then this value is assumed to be the host.
#If you're using PostgreSQL, an empty string means to use a Unix domain socket for the connection, rather than a network connection to localhost. If you explicitly need to use a TCP/IP connection on the local machine with PostgreSQL, specify localhost here.

NAME = ''
#Default: '' (Empty string)
#The name of the database to use. For SQLite, it's the full path to the database file. When specifying the path, always use forward slashes, even on Windows (e.g. C:/homes/user/mysite/sqlite3.db).

OPTIONS = ''
#Default: {} (Empty dictionary)
#Extra parameters to use when connecting to the database. Consult backend module's document for available keywords.

PASSWORD = ''
#Default: '' (Empty string)
#The password to use when connecting to the database. Not used with SQLite.

PORT = ''
#Default: '' (Empty string)
#The port to use when connecting to the database. An empty string means the default port. Not used with SQLite.

USER = ''
#Default: '' (Empty string)
#The username to use when connecting to the database. Not used with SQLite.

TEST_CHARSET = None
#Default: None
#The character set encoding used to create the test database. The value of this string is passed directly through to the database, so its format is backend-specific.
#Supported for the PostgreSQL (postgresql, postgresql_psycopg2) and MySQL (mysql) backends.

TEST_COLLATION = None
#Default: None
#The collation order to use when creating the test database. This value is passed directly to the backend, so its format is backend-specific.
#Only supported for the mysql backend (see the MySQL manual for details).

TEST_MIRROR = None
#Default: None
#The alias of the database that this database should mirror during testing.
#This setting exists to allow for testing of master/slave configurations of multiple databases. See the documentation on testing master/slave configurations for details.

TEST_NAME = None
#Default: None
#The name of database to use when running the test suite.
#If the default value (None) is used with the SQLite database engine, the tests will use a memory resident database. For all other database engines the test database will use the name 'test_' + DATABASE_NAME.
#See Testing Django applications.

DATABASE_ROUTERS = []
#Default: [] (Empty list)
#The list of routers that will be used to determine which database to use when performing a database queries.
#See the documentation on automatic database routing in multi database configurations.

DATE_FORMAT = ''
#Default: 'N j, Y' (e.g. Feb. 4, 2003)
#The default formatting to use for date fields in any part of the system. Note that if USE_L10N is set to True, then locale format will be applied. See allowed date format strings.
#See also DATETIME_FORMAT, TIME_FORMAT and SHORT_DATE_FORMAT.

DATE_INPUT_FORMATS = ''
#Default:
#('%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y',
#'%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y',
#'%B %d, %Y', '%d %B %Y', '%d %B, %Y')
#A tuple of formats that will be accepted when inputting data on a date field. Formats will be tried in order, using the first valid. Note that these format strings are specified in Python's datetime module syntax, that is different from the one used by Django for formatting dates to be displayed.
#See also DATETIME_INPUT_FORMATS and TIME_INPUT_FORMATS.

DATETIME_FORMAT = ''
#Default: 'N j, Y, P' (e.g. Feb. 4, 2003, 4 p.m.)
#The default formatting to use for datetime fields in any part of the system. Note that if USE_L10N is set to True, then locale format will be applied. See allowed date format strings.
#See also DATE_FORMAT, TIME_FORMAT and SHORT_DATETIME_FORMAT.

DATETIME_INPUT_FORMATS = ''
#Default:
#('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
#'%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M', '%m/%d/%Y',
#'%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M', '%m/%d/%y')
#A tuple of formats that will be accepted when inputting data on a datetime field. Formats will be tried in order, using the first valid. Note that these format strings are specified in Python's datetime module syntax, that is different from the one used by Django for formatting dates to be displayed.
#See also DATE_INPUT_FORMATS and TIME_INPUT_FORMATS.

DEBUG = ''
#Default: False
#A boolean that turns on/off debug mode.
#If you define custom settings, django/views/debug.py has a HIDDEN_SETTINGS regular expression which will hide from the DEBUG view anything that contains 'SECRET', 'PASSWORD', or 'PROFANITIES'. This allows untrusted users to be able to give backtraces without seeing sensitive (or offensive) settings.
#Still, note that there are always going to be sections of your debug output that are inappropriate for public consumption. File paths, configuration options, and the like all give attackers extra information about your server.
#It is also important to remember that when running with DEBUG turned on, Django will remember every SQL query it executes. This is useful when you are debugging, but on a production server, it will rapidly consume memory.
#Never deploy a site into production with DEBUG turned on.

DEBUG_PROPAGATE_EXCEPTIONS = ''
#New in Django 1.0: Please, see the release notes
#Default: False
#If set to True, Django's normal exception handling of view functions will be suppressed, and exceptions will propagate upwards. This can be useful for some test setups, and should never be used on a live site.

DECIMAL_SEPARATOR = ''
#Default: '.' (Dot)
#Default decimal separator used when formatting decimal numbers.

DEFAULT_CHARSET = ''
#Default: 'utf-8'
#Default charset to use for all HttpResponse objects, if a MIME type isn't manually specified. Used with DEFAULT_CONTENT_TYPE to construct the Content-Type header.

DEFAULT_CONTENT_TYPE = ''
#Default: 'text/html'
#Default content type to use for all HttpResponse objects, if a MIME type isn't manually specified. Used with DEFAULT_CHARSET to construct the Content-Type header.

DEFAULT_FILE_STORAGE = ''
#Default: 'django.core.files.storage.FileSystemStorage'
#Default file storage class to be used for any file-related operations that don't specify a particular storage system. See Managing files.

DEFAULT_FROM_EMAIL = ''
#Default: 'webmaster@localhost'
#Default e-mail address to use for various automated correspondence from the site manager(s).

DEFAULT_TABLESPACE = ''
#New in Django 1.0: Please, see the release notes
#Default: '' (Empty string)
#Default tablespace to use for models that don't specify one, if the backend supports it.

DEFAULT_INDEX_TABLESPACE = ''
#New in Django 1.0: Please, see the release notes
#Default: '' (Empty string)
#Default tablespace to use for indexes on fields that don't specify one, if the backend supports it.

DISALLOWED_USER_AGENTS = ''
#Default: () (Empty tuple)
#List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bad robots/crawlers. This is only used if CommonMiddleware is installed (see Middleware).

EMAIL_BACKEND = ''
#New in Django Development version.
#Default: 'django.core.mail.backends.smtp'
#The backend to use for sending emails. For the list of available backends see Sending e-mail.

EMAIL_FILE_PATH = ''
#New in Django Development version.
#Default: Not defined
#The directory used by the file email backend to store output files.

EMAIL_HOST = ''
#Default: 'localhost'
#The host to use for sending e-mail.
#See also EMAIL_PORT.

EMAIL_HOST_PASSWORD = ''
#Default: '' (Empty string)
#Password to use for the SMTP server defined in EMAIL_HOST. This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server. If either of these settings is empty, Django won't attempt authentication.
#See also EMAIL_HOST_USER.

EMAIL_HOST_USER = ''
#Default: '' (Empty string)
#Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won't attempt authentication.
#See also EMAIL_HOST_PASSWORD.

EMAIL_PORT = ''
#Default: 25
#Port to use for the SMTP server defined in EMAIL_HOST.

EMAIL_SUBJECT_PREFIX = ''
#Default: '[Django] '
#Subject-line prefix for e-mail messages sent with django.core.mail.mail_admins or django.core.mail.mail_managers. You'll probably want to include the trailing space.

EMAIL_USE_TLS = ''
#New in Django 1.0: Please, see the release notes
#Default: False
#Whether to use a TLS (secure) connection when talking to the SMTP server.

FILE_CHARSET = ''
#New in Django 1.0: Please, see the release notes
#Default: 'utf-8'
#The character encoding used to decode any files read from disk. This includes template files and initial SQL data files.

FILE_UPLOAD_HANDLERS = ''
#New in Django 1.0: Please, see the release notes
#Default:
#("django.core.files.uploadhandler.MemoryFileUploadHandler",
 #"django.core.files.uploadhandler.TemporaryFileUploadHandler",)
#A tuple of handlers to use for uploading. See Managing files for details.

FILE_UPLOAD_MAX_MEMORY_SIZE = ''
#New in Django 1.0: Please, see the release notes
#Default: 2621440 (i.e. 2.5 MB).
#The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See Managing files for details.

FILE_UPLOAD_TEMP_DIR = ''
#New in Django 1.0: Please, see the release notes
#Default: None
#The directory to store data temporarily while uploading files. If None, Django will use the standard temporary directory for the operating system. For example, this will default to '/tmp' on *nix-style operating systems.
#See Managing files for details.

FILE_UPLOAD_PERMISSIONS = ''
#Default: None
#The numeric mode (i.e. 0644) to set newly uploaded files to. For more information about what these modes mean, see the documentation for os.chmod
#If this isn't given or is None, you'll get operating-system dependent behavior. On most platforms, temporary files will have a mode of 0600, and files saved from memory will be saved using the system's standard umask.

FIRST_DAY_OF_WEEK = ''
#Default: 0 (Sunday)
#Number representing the first day of the week. This is especially useful when displaying a calendar. This value is only used when not using format internationalization, or when a format cannot be found for the current locale.
#The value must be an integer from 0 to 6, where 0 means Sunday, 1 means Monday and so on.

FIXTURE_DIRS = ''
#Default: () (Empty tuple)
#List of locations of the fixture data files, in search order. Note that these paths should use Unix-style forward slashes, even on Windows. See Testing Django applications.

FORCE_SCRIPT_NAME = ''
#Default: None
#If not None, this will be used as the value of the SCRIPT_NAME environment variable in any HTTP request. This setting can be used to override the server-provided value of SCRIPT_NAME, which may be a rewritten version of the preferred value or not supplied at all.

FORMAT_MODULE_PATH = ''
#Default: None
#A full Python path to a Python package that contains format definitions for project locales. If not None, Django will check for a formats.py file, under the directory named as the current locale, and will use the formats defined on this file.
#For example, if FORMAT_MODULE_PATH is set to mysite.formats, and current language is en (English), Django will expect a directory tree like:
# mysite/
#     formats/
#         __init__.py
#         en/
#             __init__.py
#             formats.py
#Available formats are DATE_FORMAT, TIME_FORMAT, DATETIME_FORMAT, YEAR_MONTH_FORMAT, MONTH_DAY_FORMAT, SHORT_DATE_FORMAT, SHORT_DATETIME_FORMAT, FIRST_DAY_OF_WEEK, DECIMAL_SEPARATOR, THOUSAND_SEPARATOR and NUMBER_GROUPING.

IGNORABLE_404_ENDS = ''
#Default: ('mail.pl', 'mailform.pl', 'mail.cgi', 'mailform.cgi', 'favicon.ico', '.php')
#See also IGNORABLE_404_STARTS and Error reporting via e-mail.

IGNORABLE_404_STARTS = ''
#Default: ('/cgi-bin/', '/_vti_bin', '/_vti_inf')
#A tuple of strings that specify beginnings of URLs that should be ignored by the 404 e-mailer. See SEND_BROKEN_LINK_EMAILS, IGNORABLE_404_ENDS and the Error reporting via e-mail.

INSTALLED_APPS = ''
#Default: () (Empty tuple)
#A tuple of strings designating all applications that are enabled in this Django installation. Each string should be a full Python path to a Python package that contains a Django application, as created by django-admin.py startapp.

INTERNAL_IPS = ''
#Default: () (Empty tuple)
#A tuple of IP addresses, as strings, that:
#See debug comments, when DEBUG is True
#Receive X headers if the XViewMiddleware is installed (see Middleware)

LANGUAGE_CODE = ''
#Default: 'en-us'
#A string representing the language code for this installation. This should be in standard language format. For example, U.S. English is "en-us". See Internationalization.

LANGUAGE_COOKIE_NAME = ''
#New in Django 1.0: Please, see the release notes
#Default: 'django_language'
#The name of the cookie to use for the language cookie. This can be whatever you want (but should be different from SESSION_COOKIE_NAME). See Internationalization.

LANGUAGES = ''
#Default: A tuple of all available languages. This list is continually growing and including a copy here would inevitably become rapidly out of date. You can see the current list of translated languages by looking in django/conf/global_settings.py (or view the online source).
#The list is a tuple of two-tuples in the format (language code, language name) -- for example, ('ja', 'Japanese'). This specifies which languages are available for language selection. See Internationalization.
#Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages.
#If you define a custom LANGUAGES setting, it's OK to mark the languages as translation strings (as in the default value displayed above) -- but use a "dummy" gettext() function, not the one in django.utils.translation. You should never import django.utils.translation from within your settings file, because that module in itself depends on the settings, and that would cause a circular import.
#The solution is to use a "dummy" gettext() function. Here's a sample settings file:
# gettext = lambda s: s
# LANGUAGES = (
#     ('de', gettext('German')),
#     ('en', gettext('English')),
# )
#With this arrangement, django-admin.py makemessages will still find and mark these strings for translation, but the translation won't happen at runtime -- so you'll have to remember to wrap the languages in the real gettext() in any code that uses LANGUAGES at runtime.

LOCALE_PATHS = ''
#Default: () (Empty tuple)
#A tuple of directories where Django looks for translation files. See Using translations in your own projects.

LOGIN_REDIRECT_URL = ''
#New in Django 1.0: Please, see the release notes
#Default: '/accounts/profile/'
#The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter.
#This is used by the login_required() decorator, for example.

LOGIN_URL = ''
#New in Django 1.0: Please, see the release notes
#Default: '/accounts/login/'
#The URL where requests are redirected for login, especially when using the login_required() decorator.

LOGOUT_URL = ''
#New in Django 1.0: Please, see the release notes
#Default: '/accounts/logout/'
#LOGIN_URL counterpart.

MANAGERS = ''
#Default: () (Empty tuple)
#A tuple in the same format as ADMINS that specifies who should get broken-link notifications when SEND_BROKEN_LINK_EMAILS=True.

MEDIA_ROOT = ''
#Default: '' (Empty string)
#Absolute path to the directory that holds media for this installation. Example: "/home/media/media.lawrence.com/" See also MEDIA_URL.

MEDIA_URL = ''
#Default: '' (Empty string)
#URL that handles the media served from MEDIA_ROOT. Example: "http://media.lawrence.com"
#Note that this should have a trailing slash if it has a path component.
#Good: "http://www.example.com/static/" Bad: "http://www.example.com/static"

MESSAGE_LEVEL = ''
#New in Django Development version.
#Default: messages.INFO
#Sets the minimum message level that will be recorded by the messages framework. See the messages documentation for more details.

MESSAGE_STORAGE = ''
#New in Django Development version.
#Default: 'django.contrib.messages.storage.user_messages.LegacyFallbackStorage'
#Controls where Django stores message data. See the messages documentation for more details.

MESSAGE_TAGS = ''
#New in Django Development version.
#Default:
#{messages.DEBUG: 'debug',
#messages.INFO: 'info',
#messages.SUCCESS: 'success',
#messages.WARNING: 'warning',
#messages.ERROR: 'error',}
#Sets the mapping of message levels to message tags. See the messages documentation for more details.

MIDDLEWARE_CLASSES = ''
#Default:
#('django.middleware.common.CommonMiddleware',
 #'django.contrib.sessions.middleware.SessionMiddleware',
 #'django.middleware.csrf.CsrfViewMiddleware',
 #'django.contrib.auth.middleware.AuthenticationMiddleware',
 #'django.contrib.messages.middleware.MessageMiddleware',)
#A tuple of middleware classes to use. See Middleware.
#Changed in Django Development version: 'django.contrib.messages.middleware.MessageMiddleware' was added to the default. For more information, see the messages documentation.

MONTH_DAY_FORMAT = ''
#Default: 'F j'
#The default formatting to use for date fields on Django admin change-list pages -- and, possibly, by other parts of the system -- in cases when only the month and day are displayed.
#For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given day displays the day and month. Different locales have different formats. For example, U.S. English would say "January 1," whereas Spanish might say "1 Enero."
#See allowed date format strings. See also DATE_FORMAT, DATETIME_FORMAT, TIME_FORMAT and YEAR_MONTH_FORMAT.

NUMBER_GROUPING = ''
#Default: 0
#Number of digits grouped together on the integer part of a number. Common use is to display a thousand separator. If this setting is 0, then, no grouping will be applied to the number. If this setting is greater than 0 then the setting THOUSAND_SEPARATOR will be used as the separator between those groups.
#See also THOUSAND_SEPARATOR

PREPEND_WWW = ''
#Default: False
#Whether to prepend the "www." subdomain to URLs that don't have it. This is only used if CommonMiddleware is installed (see Middleware). See also APPEND_SLASH.

PROFANITIES_LIST = ''
#A tuple of profanities, as strings, that will trigger a validation error when the hasNoProfanities validator is called.
#We don't list the default values here, because that would be profane. To see the default values, see the file django/conf/global_settings.py.

ROOT_URLCONF = ''
#Default: Not defined
#A string representing the full Python import path to your root URLconf. For example: "mydjangoapps.urls". Can be overridden on a per-request basis by setting the attribute urlconf on the incoming HttpRequest object. See How Django processes a request for details.

SECRET_KEY = ''
#Default: '' (Empty string)
#A secret key for this particular Django installation. Used to provide a seed in secret-key hashing algorithms. Set this to a random string -- the longer, the better. django-admin.py startproject creates one automatically.

SEND_BROKEN_LINK_EMAILS = ''
#Default: False
#Whether to send an e-mail to the MANAGERS each time somebody visits a Django-powered page that is 404ed with a non-empty referer (i.e., a broken link). This is only used if CommonMiddleware is installed (see Middleware. See also IGNORABLE_404_STARTS, IGNORABLE_404_ENDS and Error reporting via e-mail.

SERIALIZATION_MODULES = ''
#Default: Not defined.
#A dictionary of modules containing serializer definitions (provided as strings), keyed by a string identifier for that serialization type. For example, to define a YAML serializer, use:
#SERIALIZATION_MODULES = { 'yaml' : 'path.to.yaml_serializer' }

SERVER_EMAIL = ''
#Default: 'root@localhost'
#The e-mail address that error messages come from, such as those sent to ADMINS and MANAGERS.

SESSION_ENGINE = ''
#New in Django 1.0: Please, see the release notes
#Default: django.contrib.sessions.backends.db
#Controls where Django stores session data. Valid values are:
#'django.contrib.sessions.backends.db'
#'django.contrib.sessions.backends.file'
#'django.contrib.sessions.backends.cache'
#See How to use sessions.

SESSION_COOKIE_AGE = ''
#Default: 1209600 (2 weeks, in seconds)
#The age of session cookies, in seconds. See How to use sessions.

SESSION_COOKIE_DOMAIN = ''
#Default: None
#The domain to use for session cookies. Set this to a string such as ".lawrence.com" for cross-domain cookies, or use None for a standard domain cookie. See the How to use sessions.

SESSION_COOKIE_NAME = ''
#Default: 'sessionid'
#The name of the cookie to use for sessions. This can be whatever you want (but should be different from LANGUAGE_COOKIE_NAME). See the How to use sessions.

SESSION_COOKIE_PATH = ''
#New in Django 1.0: Please, see the release notes
#Default: '/'
#The path set on the session cookie. This should either match the URL path of your Django installation or be parent of that path.
#This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths, and each instance will only see its own session cookie.

SESSION_COOKIE_SECURE = ''
#Default: False
#Whether to use a secure cookie for the session cookie. If this is set to True, the cookie will be marked as "secure," which means browsers may ensure that the cookie is only sent under an HTTPS connection. See the How to use sessions.

SESSION_DB_ALIAS = ''
#New in Django Development version.
#Default: None
#If you're using database-backed session storage, this selects the database alias that will be used to store session data. By default, Django will use the default database, but you can store session data on any database you choose.

SESSION_EXPIRE_AT_BROWSER_CLOSE = ''
#Default: False
#Whether to expire the session when the user closes his or her browser. See the How to use sessions.

SESSION_FILE_PATH = ''
#New in Django 1.0: Please, see the release notes
#Default: None
#If you're using file-based session storage, this sets the directory in which Django will store session data. See How to use sessions. When the default value (None) is used, Django will use the standard temporary directory for the system.

SESSION_SAVE_EVERY_REQUEST = ''
#Default: False
#Whether to save the session data on every request. See How to use sessions.

SHORT_DATE_FORMAT = ''
#Default: m/d/Y (e.g. 12/31/2003)
#An available formatting that can be used for date fields on templates. Note that if USE_L10N is set to True, then locale format will be applied. See allowed date format strings.
#See also DATE_FORMAT and SHORT_DATETIME_FORMAT.

SHORT_DATETIME_FORMAT = ''
#Default: m/d/Y P (e.g. 12/31/2003 4 p.m.)
#An available formatting that can be used for datetime fields on templates. Note that if USE_L10N is set to True, then locale format will be applied. See allowed date format strings.
#See also DATE_FORMAT and SHORT_DATETIME_FORMAT.

SITE_ID = ''
#Default: Not defined
#The ID, as an integer, of the current site in the django_site database table. This is used so that application data can hook into specific site(s) and a single database can manage content for multiple sites.
#See The "sites" framework.

TEMPLATE_CONTEXT_PROCESSORS = ''
#Default:
#("django.core.context_processors.auth",
#"django.core.context_processors.debug",
#"django.core.context_processors.i18n",
#"django.core.context_processors.media",
#"django.contrib.messages.context_processors.messages")
#A tuple of callables that are used to populate the context in RequestContext. These callables take a request object as their argument and return a dictionary of items to be merged into the context.
#Changed in Django Development version: "django.contrib.messages.context_processors.messages" was added to the default. For more information, see the messages documentation.

TEMPLATE_DEBUG = ''
#Default: False
#A boolean that turns on/off template debug mode. If this is True, the fancy error page will display a detailed report for any TemplateSyntaxError. This report contains the relevant snippet of the template, with the appropriate line highlighted.
#Note that Django only displays fancy error pages if DEBUG is True, so you'll want to set that to take advantage of this setting.
#See also DEBUG.

TEMPLATE_DIRS = ''
#Default: () (Empty tuple)
#List of locations of the template source files, in search order. Note that these paths should use Unix-style forward slashes, even on Windows.
#See The Django template language..

TEMPLATE_LOADERS = ''
#Default:
#('django.template.loaders.filesystem.Loader',
 #'django.template.loaders.app_directories.Loader')
#A tuple of template loader classes, specified as strings. Each Loader class knows how to import templates from a particular sources. Optionally, a tuple can be used instead of a string. The first item in the tuple should be the Loader's module, subsequent items are passed to the Loader during initialization. See The Django template language: For Python programmers.

TEMPLATE_STRING_IF_INVALID = ''
#Default: '' (Empty string)
#Output, as a string, that the template system should use for invalid (e.g. misspelled) variables. See How invalid variables are handled..

TEST_RUNNER = ''
#Default: 'django.test.simple.DjangoTestSuiteRunner'
#Changed in Django Development version: Prior to 1.2, test runners were a function, not a class.
#The name of the class to use for starting the test suite. See Testing Django applications.

THOUSAND_SEPARATOR = ''
#Default , (Comma)
#Default thousand separator used when formatting numbers. This setting is used only when NUMBER_GROUPPING is set.
#See also NUMBER_GROUPPING, DECIMAL_SEPARATOR

TIME_FORMAT = ''
#Default: 'P' (e.g. 4 p.m.)
#The default formatting to use for time fields in any part of the system. Note that if USE_L10N is set to True, then locale format will be applied. See allowed date format strings.
#See also DATE_FORMAT and DATETIME_FORMAT.

TIME_INPUT_FORMATS = ''
#Default: ('%H:%M:%S', '%H:%M')
#A tuple of formats that will be accepted when inputting data on a time field. Formats will be tried in order, using the first valid. Note that these format strings are specified in Python's datetime module syntax, that is different from the one used by Django for formatting dates to be displayed.
#See also DATE_INPUT_FORMATS and DATETIME_INPUT_FORMATS.

TIME_ZONE = ''
#Default: 'America/Chicago'
#A string representing the time zone for this installation. See available choices. (Note that list of available choices lists more than one on the same line; you'll want to use just one of the choices for a given time zone. For instance, one line says 'Europe/London GB GB-Eire', but you should use the first bit of that -- 'Europe/London' -- as your TIME_ZONE setting.)
#Note that this is the time zone to which Django will convert all dates/times -- not necessarily the timezone of the server. For example, one server may serve multiple Django-powered sites, each with a separate time-zone setting.
#Normally, Django sets the os.environ['TZ'] variable to the time zone you specify in the TIME_ZONE setting. Thus, all your views and models will automatically operate in the correct time zone. However, if you're manually manually configuring settings, Django will not touch the TZ environment variable, and it'll be up to you to ensure your processes are running in the correct environment.

URL_VALIDATOR_USER_AGENT = ''
#Default: Django/<version> (http://www.djangoproject.com/)
#The string to use as the User-Agent header when checking to see if URLs exist (see the verify_exists option on URLField).

USE_ETAGS = ''
#Default: False
#A boolean that specifies whether to output the "Etag" header. This saves bandwidth but slows down performance. This is only used if CommonMiddleware is installed (see Middleware).

USE_L10N = ''
#Default False
#A boolean that specifies if data will be localized by default or not. If this is set to True, e.g. Django will display numbers and dates using the format of the current locale.
#See also USE_I18N and LANGUAGE_CODE

USE_I18N = ''
#Default: True
#A boolean that specifies whether Django's internationalization system should be enabled. This provides an easy way to turn it off, for performance. If this is set to False, Django will make some optimizations so as not to load the internationalization machinery.
#See also USE_L10N

USE_THOUSAND_SEPARATOR = ''
#Default False
#A boolean that specifies wheter to display numbers using a thousand separator. If this is set to True, Django will use values from THOUSAND_SEPARATOR and NUMBER_GROUPING from current locale, to format the number. USE_L10N must be set to True, in order to format numbers.
#See also THOUSAND_SEPARATOR and NUMBER_GROUPING.

YEAR_MONTH_FORMAT = ''
#Default: 'F Y'
#The default formatting to use for date fields on Django admin change-list pages -- and, possibly, by other parts of the system -- in cases when only the year and month are displayed.
#For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given month displays the month and the year. Different locales have different formats. For example, U.S. English would say "January 2006," whereas another locale might say "2006/January."
#See allowed date format strings. See also DATE_FORMAT, DATETIME_FORMAT, TIME_FORMAT and MONTH_DAY_FORMAT.

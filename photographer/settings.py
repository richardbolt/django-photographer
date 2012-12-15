# Django settings for django-photographer - deployment with Heroku.
import os
import sys
import urlparse

import django.conf.global_settings as DEFAULT_SETTINGS
import dj_database_url


DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (os.environ.get('ADMIN_NAME', ''), os.environ.get('ADMIN_EMAIL', '')),
)

MANAGERS = ADMINS

RB_SITE_TITLE = os.environ.get('RB_SITE_TITLE', '')
RB_THEME = os.environ.get('RB_THEME', 'plain')
RB_SITE_URL = os.environ.get('RB_SITE_URL', '/')
RB_BLOG_RSS_URL = os.environ.get('RB_BLOG_RSS_URL', '/blog/feed/')
BLOG_TITLE = os.environ.get('BLOG_TITLE', RB_SITE_TITLE)
BLOG_DESCRIPTION = os.environ.get('BLOG_DESCRIPTION', 'The blog of '+RB_SITE_TITLE)
RB_FACEBOOK = os.environ.get('RB_FACEBOOK', '')
RB_TWITTER_HANDLE = os.environ.get('RB_TWITTER_HANDLE', '')
# Template names:
RB_TEMPLATE_BASE = os.environ.get('RB_TEMPLATE_BASE', 'base.html')
RB_TEMPLATE_HEAD = os.environ.get('RB_TEMPLATE_HEAD', '_head.html')
RB_TEMPLATE_HEADER = os.environ.get('RB_TEMPLATE_HEADER', '_header.html')
RB_TEMPLATE_NAV = os.environ.get('RB_TEMPLATE_NAV', '_nav.html')
RB_TEMPLATE_FOOTER = os.environ.get('RB_TEMPLATE_FOOTER', '_footer.html')

DATABASES = DEFAULT_SETTINGS.DATABASES
try:
    # Load settings from the environment variable DATABASE_URL.
    DATABASES['default'] = dj_database_url.config()
except:
    print 'Unexpected error:', sys.exc_info()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Los_Angeles')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')

SITE_ID = int(os.environ.get('SITE_ID', 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'static')),
)

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'
AWS_QUERYSTRING_AUTH = False # Don't include auth in every url
AWS_S3_SECURE_URLS = False

AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET', '')
AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET', '')

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'  # Deprecated but required for django-admin-tools (temporarily).

if DEBUG:
    # For debug when we don't want to have to use S3.
    DEFAULT_FILE_STORAGE = DEFAULT_SETTINGS.DEFAULT_FILE_STORAGE
    STATICFILES_STORAGE = DEFAULT_SETTINGS.STATICFILES_STORAGE
    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              'mediafiles')
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              'sitestatic')

ADMIN_TOOLS_THEMING_CSS = 'themes/%s/styles/admin.css' % RB_THEME

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secretkey!JohnCleese!')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'photographer.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'photographer.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'static',
                                 'themes', RB_THEME, 'templates')),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'photographer.context_processors.defaults',
    'feincms.context_processors.add_page_if_missing',
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    's3_folder_storage',
    'gunicorn',
    'haystack',
    
    'mptt',
    'feincms',
    'feincms.module.page',
    'feincms.module.medialibrary',
    'markupmirror',
    'markupmirror.feincms',
    'form_designer',
    'elephantblog',
    
    'photographer'  # To register the feincms content modules, etc.
)

MARKUPMIRROR_DEFAULT_MARKUP_TYPE = 'markdown'

def elephantblog_entry_url_app(self):
    from feincms.content.application.models import app_reverse
    return app_reverse('elephantblog_entry_detail', 'elephantblog.urls', kwargs={
        'year': self.published_on.strftime('%Y'),
        'month': self.published_on.strftime('%m'),
        'day': self.published_on.strftime('%d'),
        'slug': self.slug,
        })

def elephantblog_categorytranslation_url_app(self):
    from feincms.content.application.models import app_reverse
    return app_reverse('elephantblog_category_detail', 'elephantblog.urls', kwargs={
        'slug': self.slug,
        })

ABSOLUTE_URL_OVERRIDES = {
    'elephantblog.entry': elephantblog_entry_url_app,
    'elephantblog.categorytranslation': elephantblog_categorytranslation_url_app,
}

BLOG_PAGINATE_BY = 10

# Search with Haystack and ElasticSearch.
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('ELASTICSEARCH_URL', ''),
        'INDEX_NAME': 'haystack',
    },
}

# Check for SendGrid for email delivery first:
if os.environ.get('SENDGRID_USERNAME') and os.environ.get('SENDGRID_PASSWORD'):
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    # Standard mail configuration: configure your env vars as required:
    EMAIL_HOST = os.environ.get('EMAIL_HOST_USER', DEFAULT_SETTINGS.EMAIL_HOST)
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', DEFAULT_SETTINGS.EMAIL_PORT))
    EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS',
                                        DEFAULT_SETTINGS.EMAIL_USE_TLS))
DEFAULT_FROM_EMAIL = os.environ.get('ADMIN_EMAIL',
                                    DEFAULT_SETTINGS.DEFAULT_FROM_EMAIL)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

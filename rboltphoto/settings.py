# Django settings for rboltphoto project - deployment with Heroku.
import os
import sys
import urlparse

import django.conf.global_settings as DEFAULT_SETTINGS


DEBUG = bool(os.environ.get('DJANGO_DEBUG', ''))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (os.environ.get('ADMIN_NAME', ''), os.environ.get('ADMIN_EMAIL', '')),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
urlparse.uses_netloc.append('postgres')
urlparse.uses_netloc.append('mysql')
try:
    if os.environ.has_key('DATABASE_URL'):
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME':     url.path[1:],
            'USER':     url.username,
            'PASSWORD': url.password,
            'HOST':     url.hostname,
            'PORT':     url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
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

ROOT_URLCONF = 'rboltphoto.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rboltphoto.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'rboltphoto.context_processors.defaults',
    'feincms.context_processors.add_page_if_missing',
)

INSTALLED_APPS = (
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
    
    'rboltphoto'  # To register the feincms content modules, etc.
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

# Search with Haystack.
# NB: You will want to use a different backend like ElasticSearch if you are
#     running something other than a small site.
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

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

RB_SITE_TITLE = os.environ.get('RB_SITE_TITLE', '')
RB_THEME = os.environ.get('RB_THEME', 'plain')
RB_SITE_URL = os.environ.get('RB_SITE_URL', '/')
RB_BLOG_RSS_URL = os.environ.get('RB_BLOG_RSS_URL', '/blog/feed/')
BLOG_TITLE = os.environ.get('BLOG_TITLE', RB_SITE_TITLE)
BLOG_DESCRIPTION = os.environ.get('BLOG_DESCRIPTION', 'The blog of '+RB_SITE_TITLE)
RB_FACEBOOK = os.environ.get('RB_FACEBOOK', '')
RB_TWITTER_HANDLE = os.environ.get('RB_TWITTER_HANDLE', '')

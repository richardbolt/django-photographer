from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import handler500
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from feincms.module.page.sitemap import PageSitemap
import markupmirror.urls


admin.autodiscover()
sitemaps = {'pages': PageSitemap}

handler500 = 'photographer.views.server_error'

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^markupmirror/', include(markupmirror.urls.preview)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    (r'^search/', include('haystack.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'', include('feincms.urls')),
)
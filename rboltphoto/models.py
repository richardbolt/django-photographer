from elephantblog.models import Entry
from feincms.module.page.models import Page
from feincms.content.application.models import ApplicationContent
from feincms.content.medialibrary.v2 import MediaFileContent
from feincms.content.raw.models import RawContent
from feincms.content.video.models import VideoContent
from form_designer.models import FormContent
from markupmirror.feincms.models import MarkupMirrorContent


Page.register_extensions('datepublisher', 'navigation', 'titles', 'seo')

Page.register_templates({
    'title': 'Standard template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    },
    {'title': 'Home page template',
    'path': 'home.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    },
    {'title': 'Portfolio page template',
    'path': 'portfolio.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    },
    {'title': 'Contact page template',
    'path': 'contact.html',
    'regions': (
        ('main', 'Main content area'),
        ('sidebar', 'Sidebar content area'),
        ),
    },
    {'title': 'Blog page template',
    'path': 'blog.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    },
    {'title': 'Search page template',
    'path': 'search/search.html',
    'regions': (
        ('main', 'Main content area'),
        ),
    }
)

MEDIAFILE_TYPE_CHOICES =(
    ('default', 'default'),
)

Page.create_content_type(MediaFileContent, TYPE_CHOICES=MEDIAFILE_TYPE_CHOICES)
Page.create_content_type(RawContent)
Page.create_content_type(VideoContent)
Page.create_content_type(FormContent)
Page.create_content_type(MarkupMirrorContent)
Page.create_content_type(ApplicationContent, APPLICATIONS=(
        ('elephantblog', 'Blog', {'urls': 'elephantblog.urls'}),
        ('haystack', 'Search', {'urls': 'haystack.urls'})
))

Entry.register_extensions('feincms.module.extensions.datepublisher',
                          'elephantblog.extensions.blogping',
)
Entry.register_regions(
    ('main', 'Main content area'),
)
Entry.create_content_type(MarkupMirrorContent, regions=('main',))
Entry.create_content_type(MediaFileContent, TYPE_CHOICES=MEDIAFILE_TYPE_CHOICES)
Entry.create_content_type(VideoContent, regions=('main',))


def defaults(request):
    from django.conf import settings
    return {
        'RB_THEME': settings.RB_THEME,
        'RB_SITE_URL': settings.RB_SITE_URL,
        'RB_BLOG_RSS_URL': settings.RB_BLOG_RSS_URL,
        'RB_SITE_TITLE': settings.RB_SITE_TITLE,
        'RB_FACEBOOK': settings.RB_FACEBOOK,
        'RB_TWITTER_HANDLE': settings.RB_TWITTER_HANDLE
    }
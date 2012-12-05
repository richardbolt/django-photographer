import os

from django import template
from django.conf import settings


register = template.Library()

@register.simple_tag(takes_context=True)
def rb_theme_includes(context):
    """
    Usage:
    {% rb_theme_includes %}
    
    Adds a file named `include.html` from the current template directory. It
    is parsed like any other Django template and popped right into the
    calling template (usually the base template base.html).
    
    This is used to include extra head items like stylesheets and javascript
    libraries specific to a given theme for more customization than pure css
    would allow.
    
    """
    content = ''
    include_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
            '..', 'static', 'themes', context['RB_THEME'], 'include.html'))
    if os.path.isfile(include_file):
        tpl = template.Template(open(include_file).read())
        content = tpl.render(context)
    return content
    
    
    
    
    
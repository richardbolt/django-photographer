import os

from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag(takes_context=True)
def rb_theme_include(context, template_name):
    """
    Usage:
    {% rb_include '_footer.html' %}

    Adds a file named `template_name` (`_footer.html` in the example) from
    the current template directory. It is parsed like any other Django
    template and popped right into the calling template (usually the base
    template base.html). As a fallback, if the `template_name` does not
    exist in the theme root directory, then the root template directory is
    searched.

    This is used to allow a given theme for more customization than pure css
    would allow.

    """
    content = ''
    root_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
            '..', 'templates', template_name))
    include_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
            '..', 'static', 'themes', context['RB_THEME'],
            template_name))
    if os.path.isfile(include_file):
        tpl = template.Template(open(include_file).read())
        content = tpl.render(context)
    elif os.path.isfile(root_file):
        tpl = template.Template(open(root_file).read())
        content = tpl.render(context)
    return content


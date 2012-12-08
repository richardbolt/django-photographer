import os

from django import template
from django.template.loader import get_template
from django.conf import settings


register = template.Library()


@register.simple_tag(takes_context=True)
def rb_theme_include(context, template_name):
    """
    Usage example:
        
        {% rb_theme_include '_header.html' %}

    Like the standard {% include %} template tag, but does not raise an
    exception if the given template does not exist in the TEMPLATE_DIRS
    search path.

    This is used to allow a given theme for more customization than pure css
    would allow and to allow for files that re not included with the base
    template to easily be included by other themes without having to override
    the base template.

    """
    try:
        tpl = get_template(template_name)
        content = tpl.render(context)
    except template.TemplateDoesNotExist:
        content = ''
    return content


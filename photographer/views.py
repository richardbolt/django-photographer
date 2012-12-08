from django.shortcuts import render_to_response
from django.template import RequestContext


def server_error(request, template_name='500.html'):
    """
    500 error handler that uses current context - so we can have a pretty page
    with the site theming intact.

    Templates: `500.html`
    Context: RequestContext
    
    """
    return render_to_response(template_name,
        context_instance = RequestContext(request)
    )
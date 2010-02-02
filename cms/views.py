#coding=utf-8
from models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe

DEFAULT_TEMPLATE = 'flatpages/default.html'

def static_view(request, url):
    """
    Page view.
    """
#    if not url.endswith('/') and settings.APPEND_SLASH:
#        return HttpResponseRedirect("%s/" % request.path)
#    if not url.startswith('/'):
#        url = "/" + url

    p = get_object_or_404(Page, url__exact=url)
    t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    p.title = mark_safe(p.title)
    p.content = mark_safe(p.content)

    c = RequestContext(request, {
        'flatpage': p,
    })
    response = HttpResponse(t.render(c))
    return response

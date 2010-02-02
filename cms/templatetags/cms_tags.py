import os
import urlparse
from django import template
from django.contrib.sites.models import Site
from django.conf import settings

register = template.Library()

def _absolute_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    domain = Site.objects.get_current().domain
    return 'http://%s%s' % (domain, url)

def _media_static(filename, base_url, base_root, flags):
    flags = set(f.strip() for f in flags.split(','))
    url = urlparse.urljoin(base_url, filename)
    if 'absolute' in flags:
        url = _absolute_url(url)
    if (filename.endswith('.css') or filename.endswith('.js')) and 'no-timestamp' not in flags or \
       'timestamp' in flags:
        fullname = os.path.join(base_root, filename)
        if os.path.exists(fullname):
            url += '?%d' % os.path.getmtime(fullname)
    return url

@register.simple_tag
def media(filename, flags=''):
    return _media_static(filename, settings.MEDIA_URL, settings.MEDIA_ROOT, flags)
    
@register.simple_tag
def static(filename, flags=''):
    return _media_static(filename, settings.STATIC_URL, settings.STATIC_ROOT, flags)    

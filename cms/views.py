#coding=utf-8
from models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from libs.shortcuts import render_to
import cjson


DEFAULT_TEMPLATE = 'cms/default.html'

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


def send_ajax(data='', message='', error=''):
    return HttpResponse(cjson.encode({
                                      'data': data,
                                      'message': message,
                                      'error': error,
                                      }))
def send_error(error):
    return send_ajax(error=error)
def send_message(message):
    return send_ajax(message=message)

def get_id(requset, s):
    try:
        return int(requset.REQUEST.get(s, '_').split('_', 1)[1])
    except:
        return 0
    
def cms_pages(requset):
    if not requset.method=='POST':
        return send_error('Error! Must be POST!')
    
    id = get_id(requset, 'id')
    target = get_id(requset, 'target')
    position = requset.REQUEST.get('position', '')
    if id and target and position in ('left', 'right', 'last-child'):
        try:       
            page = Page.objects.get(id=id)
            target_page = Page.objects.get(id=target)
            page.move_to(target_page, position)
            return send_message(u'Страница успешно перемещена!')
        
        except Page.DoesNotExist:
            return send_error('Error! Page Does not exist!')
        
        
    elif id and not target and not position:
        data = []
        for object in Page.active_objects.filter(parent=id):
            data.append({
                         'attributes': {'id': 'page_%s' % object.id,  }, 
                         'data': { 
                                  'title': object.name, 
                                  'attributes': {'class': 'page', 'href': '%s/' % object.id} 
                                  },
                         'state': object.get_descendant_count() and "closed" or "opened",
                         'children': []
                         })            
            
        return send_ajax(data)
   
    else:
        return send_error('Error in params!')
    
@render_to('site_map.html')
def site_map(request):
    return {'object_list': Page.active_objects.all()}

@render_to('search.html')
def search(request):
    return {}
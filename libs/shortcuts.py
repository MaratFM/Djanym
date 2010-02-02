from django.http import HttpResponse
from django.conf import settings
from django.template.context import RequestContext
from functools import wraps
from django.shortcuts import render_to_response

default_mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE')

def render_to(prefix=None):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            response = func(request, *args, **kwargs)

            template_name = ''
            mimetype = default_mimetype
            context_processors = {}
 
            if isinstance(response, HttpResponse):
                return response

            elif isinstance(response, basestring):
                if prefix:
                    #@render_to('template.html')
                    #def view_name(request):
                    #    return 'Content of the page'
                    template_name = prefix
                    context_processors = {'content': response}
                else:
                    #@render_to
                    #def view_name(request):
                    #    return '<html><body>Content of the page</body></html>'
                    return HttpResponse(response)
            
            elif isinstance(response, (tuple, list)):
                len_tuple = len(response)
                if len_tuple == 2:
                    #@render_to
                    #def view_name(request):
                    #    return ('template.html', {'content': 'Content of the page'})
                    template_name, context_processors = response
                    mimetype = default_mimetype
                elif len_tuple == 3:
                    #@render_to
                    #def view_name(request):
                    #    return ('template.html', {'content': 'Content of the page'}, 'txt')
                    template_name, context_processors, mimetype = response
            
            elif isinstance(response, (dict)):
                if prefix:
                    #@render_to('template.html')
                    #def view_name(request):
                    #    return {'content': 'Content of the page'}
                    template_name = prefix
                    context_processors = response
                elif response.get('template'):
                    #@render_to
                    #def view_name(request):
                    #    return {'template': 'template.html', 'content': 'Content of the page'}
                    template_name = response['template']
                    context_processors = response
                else:
                    pass

            return render_to_response(correct_path(template_name),
                                      dictionary = context_processors,
                                      context_instance=RequestContext(request),
                                      mimetype = mimetype)
        return wrapper
 
    def correct_path(template_name):
        if template_name.startswith('/'):
            return template_name[1:]
        return template_name
 
    return renderer
   

   
try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

globals = local()



class GlobalsMiddleware:
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""
    def process_request(self, request):
        globals.request = request        
        globals.user = request.user

def globals_processor(request):
    return {'globals': globals}

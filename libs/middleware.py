from libs.globals import globals

class GlobalsMiddleware:
    """Middleware that gets various objects from the
    request object and saves them in thread local storage."""
    def process_request(self, request):
        globals.request = request        
        globals.user = request.user
        
        
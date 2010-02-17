#coding=utf-8
from models import Page
from djanym.libs.globals import globals
from interprocess import interprocess, log_threaded
from constants import *
from menu import init_menu, get_page, get_breadcrumbs

class CMSMiddleware:
    '''
    Middleware устанавливает переменные в globals
    необходимые для вывода меню и навигации в шаблонах
    '''
    def process_request(self, request):
        if not interprocess.comp_globals(IP_KEY_MENU):
            # Нужно обновить меню
            init_menu()
            
        globals.request = request
        globals.page = get_page(request.path)
        globals.breadcrumbs = get_breadcrumbs(globals.page)        

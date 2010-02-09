from django.http import Http404
from django.conf import settings
from models import Page
from djanym.libs.globals import globals
from copy import copy, deepcopy
from django.core.cache import cache

class MenuNode():
    def __init__(self, page, level=0, parent=None, children=[]):
        self.page = page
        self.children = children
        self.parent = parent
        self.level = level
        self.leaf = False    
        
        if page.type==0 or page.type==4:
            self.leaf = True
        
        if page.type==2:
            url = self.page.link.url
        else:
            url = self.page.url
        
        if not url:
            self.url = '/'
        elif page.type==4:
            self.url = self.page.title
        else: 
            self.url = '/%s/' % url
    
    @property
    def selected(self):
        try:        
            return self==globals.breadcrumbs[self.level]
        except (AttributeError, IndexError):
            return False        

    @property
    def current(self):
        if self.page.type==1 and self==getattr(globals, 'page', None):
            return globals.request.path == self.url
        else:
            return self==getattr(globals, 'page', None)
        
    def print_recursive(self, prefix=''):
        out = [prefix+self.__unicode__()]
        for child in self.children:
            out.append( child.print_recursive(prefix+'--- ') )
        return ''.join(out)
    
    def __str__(self):
        return self.page.name
    
    def __unicode__(self):
        return '%s: %s = "%s" [%s] %s %s [%s %s]' % (self.page.id, 
                                      self.page.url,
                                      self.page.name, 
                                      self.parent.__str__(),
                                      self.level,
                                      self.leaf,
                                      self.selected,
                                      self.current,
                                      ) 
        

def build_menu(query_set, level=0, parent=None):
    items = []
    for page in query_set:
        item = MenuNode(page, level, parent)
        items.append( item )
        globals.menu_list.append( item ) 
   
        if page.get_descendant_count():
            item.children = build_menu(page.get_children().filter(status=1), level+1, item)
    return items

def get_page(path):
    if path.endswith('/'): path = path[:-1]
    if path.startswith('/'): path = path[1:]
    for menu in reversed(globals.menu_list):
        if menu.leaf and menu.page.url==path:
            return menu
        elif not menu.leaf and path.startswith(menu.page.url):
            return menu

def get_breadcrumbs(item):
    out = [item]
    if item and item.parent:
        out = get_breadcrumbs(item.parent)+out
    return out


class CMSMiddleware:
    def process_request(self, request):
        globals.page = get_page(copy(request.path))
        globals.request = request
        globals.breadcrumbs = get_breadcrumbs(globals.page)        
#        print globals.breadcrumbs
#        print '\n'.join([m.__str__() for m in globals.breadcrumbs])


def init_menu():
    globals.menu_list = []
    globals.menu_tree = build_menu(Page.active_objects.filter(level=0))
    print 'Init menu...'

init_menu()

#print ''.join([m.print_recursive('\n') for m in menu_tree])
#print '\n\n', '\n'.join([m.__unicode__() for m in menu_list])


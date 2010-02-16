#coding=utf-8
from django.http import Http404
from django.conf import settings
from models import Page
from djanym.libs.globals import globals
from copy import copy, deepcopy
from django.core.cache import cache
from interprocess import interprocess, log_threaded
from constants import *

class MenuNode(object):
    '''
    Класс пункта меню, необходим для построения дерева 
    меню в памяти и последующего вывода в шаблонах
    '''    
    def __init__(self, page, level=0, parent=None, children=[]):
        self.page = page
        self.name = self.page.name
        self.children = children
        self.parent = parent
        self.level = level
        self.leaf = False    
        
        if page.type==PAGE_TYPE_STATIC or page.type==PAGE_TYPE_LINK:
            self.leaf = True
        
        if page.type==PAGE_TYPE_REDIRECT:
            url = self.page.link.url
        else:
            url = self.page.url
        
        if not url:
            # Главная страница
            url = '/'
        elif page.type==PAGE_TYPE_LINK:
            # Берем ссылку из заголовка
            url = self.page.title
        else: 
            url = '/%s/' % url
        self.url = url
        
    @property
    def selected(self):
        '''
        Возвращает True если этот пункт меню присутствует в навигационном пути
        иными словами этот пункт активен либо активен один из его потомков
        '''
        try:        
            return self==globals.breadcrumbs[self.level]
        except (AttributeError, IndexError):
            return False        

    @property
    def current(self):
        '''
        Возвращает True если этот пункт меню активен, т.е. является текущей страницей
        Для приложение возвращает True только для корневой страницы приложения
        '''
        if self.page.type==PAGE_TYPE_APPLICATION and self==getattr(globals, 'page', None):
            return globals.request.path == self.url
        else:
            return self==getattr(globals, 'page', None)
    
    def __str__(self):
        return self.name   
            
#    def print_recursive(self, prefix=''):
#        out = [prefix+self.__unicode__()]
#        for child in self.children:
#            out.append( child.print_recursive(prefix+'--- ') )
#        return ''.join(out)
#    
#    def __unicode__(self):
#        return '%s: %s = "%s" [%s] %s %s [%s %s]' % (self.page.id, 
#                                      self.page.url,
#                                      self.page.name, 
#                                      self.parent.__str__(),
#                                      self.level,
#                                      self.leaf,
#                                      self.selected,
#                                      self.current,
#                                      ) 
     

def build_menu(query_set, level=0, parent=None):
    '''
    Строит дерево пунктов меню, 
    возвращает список MenuNode корневого уровня, внутренние уровни содержат 
    элементы MenuNode в свойстве children
    
    так же в процессе обработки заполняется globals.menu_list
    '''
    menu_tree = []
    for page in query_set:
        node = MenuNode(page, level, parent)
        menu_tree.append( node )
        globals.menu_list.append( node ) 
   
        if page.get_descendant_count():
            node.children = build_menu(page.get_children().filter(status=STATUS_ACTIVE), level+1, node)
    return menu_tree

def init_menu():
    '''
    Инициализирует/реинициализирует меню
    '''
    globals.menu_list = []
    globals.menu_tree = build_menu(Page.active_objects.filter(level=0))
    log_threaded ('Init menu...')  
            
def get_page(request_path):
    '''
    Возвращает MenuNode соответствующий странице с указанным путем request_path
    Для проверки используется globals.menu_list
    '''
    path = copy(request_path)
    if path.endswith('/'): path = path[:-1]
    if path.startswith('/'): path = path[1:]
    for node in reversed(globals.menu_list):
        if node.leaf and node.page.url==path:
            return node
        elif not node.leaf and path.startswith(node.page.url):
            return node

def get_breadcrumbs(node):
    '''
    Строит цепочку "хлебных крошек" для указанного MenuNode
    '''
    out = [node]
    if node and node.parent:
        out = get_breadcrumbs(node.parent)+out
    return out
#coding=utf-8
from django.conf.urls.defaults import patterns, include
from django.utils.importlib import import_module    
from views import static_view
from models import Page
from interprocess import interprocess, log_threaded
from constants import *
    
def gen_patterns():
    '''
    Функция, генерирующая urlpatterns на основе страниц полученыых из базы данных
    '''    
    urls = [] 
    for page in Page.objects.all().order_by('-tree_id', '-lft'):
        url = page.url
        
        if page.type==PAGE_TYPE_COPY:
            # Если тип страницы капия то ведем себя как будто мы - это она
            page=page.link
        
        if page.type==PAGE_TYPE_STATIC:
            # Статическая страница
            if url:
                urls.append((r'^(?P<url>%s)/$' % url, static_view ))
            else:
                # Главная страница с пустым url
                urls.append((r'^(?P<url>%s)$' % url, static_view ))
        elif page.type==PAGE_TYPE_APPLICATION:
            # Приложение
            try:
                module, attr_name = page.app_url.split(' ', 1)
            except ValueError:
                # Приложение с загрузкой паттернов из urlpatterns
                urls.append((r'^%s/' % url, include(page.app_url) ))
            else:
                # Приложение с указанием переменной хранящей патерны
                urls.append((r'^%s/' % url, include( getattr( import_module(module), attr_name) ) ))
          
        elif page.type==PAGE_TYPE_REDIRECT:
            # Перенаправление, такой страницы не существует        
            pass
        elif page.type==PAGE_TYPE_COPY:
            # Дубликат, патерны уже созданы, т.к. мы дублировали нормальную страницу
            pass
        elif page.type==PAGE_TYPE_LINK:
            # Ссылка, создавать паттерн не нужно
            pass
    
    log_threaded('Add url patterns...')
    return patterns('', *urls)

   
class cms_patterns:
    '''
    Класс реализующий логику обычной переменной urlpatterns, которая по сути является списком.
    Добавляет возможность перезагружать список страниц (urlpatterns) при необходимости
    Для проверки используется разделяемая память, которая контролируется в модуле interprocess
    '''    
    def __init__(self):
        self._patterns_cache = None
        self._version = ''
    
    def _get_url_patterns(self):
        '''
        property, который возвращает urlpatterns и при необходимости перезагружает _patterns_cache
        т.к. __iter__ вызывается при каждом запросе, то и проверка осуществляется каждый раз
        '''        
        # если текущая версия не совпадает с той что в разделяемой памяти 
        if not interprocess.comp_globals(IP_KEY_URLPATTERNS) or not self._patterns_cache:
            self._patterns_cache = gen_patterns()
        return self._patterns_cache
    url_patterns = property(_get_url_patterns)
    
    def __iter__(self):
        for p in self.url_patterns:
            yield p
            
    def __reversed__(self):
        for p in reversed(self.url_patterns):
            yield p
    
urlpatterns = cms_patterns()






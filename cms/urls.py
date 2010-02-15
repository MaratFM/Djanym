#coding=utf-8
from django.conf.urls.defaults import patterns, url as gen_url, include
from django.utils.importlib import import_module    
from views import static_view, cms_pages
from models import Page
from sub_thread import need_reload, log_threaded
    
def gen_patterns():
    # Первый аргумент функции patterns ''
    urls = [] 
    for page in Page.objects.all().order_by('-tree_id', '-lft'):
        url = page.url
        if page.type==3:
            page=page.link
        
        if page.type==0:
            # Статическая страница
            if url:
                urls.append((r'^(?P<url>%s)/$' % url, static_view ))
            else:
                urls.append((r'^(?P<url>%s)$' % url, static_view ))
        elif page.type==1:
            # Приложение
           
            module_attr = page.app_url.split(' ', 1)
#            print '----', (r'^%s/' % url, include(module_attr[0]) )
            if len(module_attr)>1:
                # Приложение с указанием модуля
                pats = getattr( import_module(module_attr[0]), module_attr[1])
                urls.append((r'^%s/' % url, include(pats) ))
            else:
                # Приложение
                urls.append(gen_url(r'^%s/' % url, include(module_attr[0]) ))
        elif page.type==2:
            # Перенаправление, такой страницы не существует        
            pass
        elif page.type==3:
            # Дубликат - страница существует
            pass
        elif page.type==4:
            # Ссылка
            pass
        else:
            pass
    
    log_threaded('Add url patterns...')
    
    urls.append(gen_url(r'^cms_ajax_pages/', cms_pages, name='cms_pages'))
    return patterns('', *urls)


    def _get_urlconf_module(self):
        try:
            return self._urlconf_module
        except AttributeError:
            self._urlconf_module = import_module(self.urlconf_name)
            return self._urlconf_module
    urlconf_module = property(_get_urlconf_module)
    
class cms_patterns:
    
    def __init__(self):
        self._patterns_cache = None
    
    def _get_url_patterns(self):
        if not self._patterns_cache or need_reload(1):
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






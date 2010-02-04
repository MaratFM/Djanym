#coding=utf-8
from django.conf.urls.defaults import *
from django.utils.importlib import import_module    
from views import static_view
from models import Page

# Первый аргумент функции patterns ''
urls = [''] 
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
        if len(module_attr)>1:
            # Приложение с указанием модуля
            pats = getattr( import_module(module_attr[0]), module_attr[1])
            urls.append((r'^%s/' % url, include(pats) ))
        else:
            # Приложение           
            urls.append((r'^%s/' % url, include(module_attr[0]) ))
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

urlpatterns = patterns(*urls)
print 'Add url patterns...'





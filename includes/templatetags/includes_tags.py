#coding=utf-8
from django import template
from includes.models import Includes
from django.utils.safestring import mark_safe
from django.core.cache import cache
register = template.Library()

@register.simple_tag
def render_include(name):
    '''
    Тэг для вывода включения
    '''
    key = ('include_'+name).replace(' ', '_')    
    content = cache.get(key)
    if content: return content
     
    obj, created = Includes.objects.get_or_create(name=name,
                  defaults={'content': name.capitalize()})
    content = mark_safe(obj.content)
    
    cache.set(key, content, 60*5)
    return content

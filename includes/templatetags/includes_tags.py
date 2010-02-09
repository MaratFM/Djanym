#coding=utf-8
from django import template
from includes.models import Includes
from django.utils.safestring import mark_safe
register = template.Library()

@register.simple_tag
def render_include(name):
    '''
    Тэг для вывода включения
    '''
    
    obj, created = Includes.objects.get_or_create(name=name,
                  defaults={'content': name.capitalize()})
    return mark_safe(obj.content)

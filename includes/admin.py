#coding=utf-8
from django.contrib import admin
from models import Includes

#===========================================================================================
#
#            I N C L U D E S
#
#===========================================================================================

class IncludesAdmin(admin.ModelAdmin):
    '''
    Класс админ. панели включаемых областей
    '''
    actions = []
    actions_on_top = False
    actions_on_bottom = True    

    list_display = ['__unicode__', ]
    list_display_links = ['__unicode__']
    list_per_page = 50
    search_fields = ['__unicode__', ]
  
    save_as = True  
    save_on_top = True
    fieldsets = (
                 ('Основные', {
                         'fields': ('name', 'content')
                         }),
    )  
  
admin.site.register(Includes, IncludesAdmin)
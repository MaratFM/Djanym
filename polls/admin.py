#coding=utf-8
from django.contrib import admin
from models import *
       
class ChoicesInline(admin.TabularInline):
    '''
    Встроенный модуль редактирования вариантов ответов
    '''    
    model = Choice
    fields = ['choice', 'sort', 'votes']
    ordering = ['sort']     
    extra = 10     
       
class PollAdmin(admin.ModelAdmin):
    actions = []
    actions_on_top = False
    actions_on_bottom = True    
    
    list_display = ['question', 'pub_date', 'status']
    list_display_links = ['question']
    list_filter  = ['status', 'pub_date']
    list_editable = ['status']
    list_per_page = 25    
    search_fields = ['question','description']
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
        
    save_as = True  
    save_on_top = True
    fieldsets = (
                 ('Основные', {
                         'fields': (
                                    'question', 
                                    ('status', 'pub_date'),
                                    'description', 
                                    )
                         }),
    )     
    inlines = (ChoicesInline,)
    
admin.site.register(Poll, PollAdmin)


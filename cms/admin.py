#coding=utf-8
from django.contrib import admin
from models import *
from tinymce.widgets import TinyMCE

class PageAdmin(admin.ModelAdmin):
    '''
    Administrative interface for Page model
    '''
    actions = []
    actions_on_top = False
    actions_on_bottom = True    
    
#    list_display = ['id', 'parents_id', 'tree_id', 'lft', 'rght', 'url', '__unicode__', 'title' ]
    list_display = ['sort', 'url', '__unicode__', 'status']#,'parent', 'title', 'type' ,'tree_id', 'lft']
    list_display_links = ['__unicode__']
    list_editable = ['sort', 'status']#, 'parent']
    list_filter = ['status']
    list_per_page = 25    
    search_fields = ['name','title']
#    ordering = ['url']
        
    save_as = True  
    save_on_top = True
    fieldsets = (
                 ('Основные', {
                         'fields': (
                                    ('parent', 'sort', 'status'),
                                    ('name', 'slug'),
                                    ('type', 'app_url', 'link'), 
                                    'title', 
                                    'content',
                                    )
                         }),
    )     
    prepopulated_fields = {'slug': ('name',)}
    
    def parents_id(self, object):
        return object.parent_id or 0
    
    class Media:
        js = ("static/js/jquery-1.3.2.js",
              "static/js/admin.js",
              "static/js/jquery.tree.js",
              )

admin.site.register(Page, PageAdmin)



#coding=utf-8
from django.contrib import admin
from models import *
from tinymce.widgets import TinyMCE
from tree_admin import MpttAdmin

class PageAdmin(MpttAdmin): #admin.ModelAdmin):
    '''
    Administrative interface for Page model
    '''
    
    tree_title_field = 'name'
    tree_display = ('name','slug','url', 'title')
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = Page    
    
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
                 ('SEO', {
                          'classes': ('collapse',),
                          'fields': (
                                     'seo_title', 
                                     'seo_description', 
                                     'seo_keywords',
                                     )
                          }),
                )     
    prepopulated_fields = {'slug': ('name',)}
 
    class Media:
        css = {
#            "all": ("extern/djanym_cms/admin.css",
#                    "extern/js_tree/themes/default/style.css"
#                    )
        }
        js = (
              "extern/jquery/jquery-1.3.2.js",
              "extern/js_tree/jquery.tree.js",
              "extern/js_tree/plugins/jquery.tree.contextmenu.js",
              "extern/djanym_cms/jstree_admin.js",
#              "extern/djanym_cms/admin.js",
              )

#    def queryset(self, request):
#        qs = self.model._default_manager.filter(level=0).order_by('tree_id', 'lft')
#        print qs
#        return qs    
    
admin.site.register(Page, PageAdmin)



#coding=utf-8
from django.contrib import admin
from models import *
from libs.widgets import AdminThumbWidget
from tinymce.widgets import TinyMCE
from libs.admin import thumbnail
       
class NewsAdmin(admin.ModelAdmin):
    actions = []
    actions_on_top = False
    actions_on_bottom = True    
    
    list_display = ['created', 'preview_image', 'name', 'status','slug']
    list_display_links = ['name']
    list_filter  = ['status', 'created']
    list_editable = ['status']
    list_per_page = 25    
    search_fields = ['name','description']
    date_hierarchy = 'created'
    ordering = ['-created']
        
    save_as = True  
    save_on_top = True
    fieldsets = (
                 ('Основные', {
                         'fields': (
                                    'name', 
                                    ('author', 'slug'), 
                                    'picture', 
                                    'anounce',
                                    'html',
                                    ('status', 'pub_date')
                                    )
                         }),
    )     
    prepopulated_fields = {'slug': ('name',)}

    
    formfield_overrides = {
#        models.TextField: {'widget': TinyMCE},
        models.ImageField: {'widget': AdminThumbWidget},        
    }

    def preview_image(self, obj):
        '''
        Поле в админке с уменьшенным изображением продукта
        '''
        return '<a href="%s/">%s</a>' % (str(obj.id), thumbnail(obj.picture))
    preview_image.short_description = u'Изобр.'
    preview_image.allow_tags = True

admin.site.register(News, NewsAdmin)




from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class TinyMCEFlatPageAdmin(FlatPageAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30}                
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)

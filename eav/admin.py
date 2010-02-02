#coding=utf-8
from django import forms
from django.contrib import admin
#from models import EAV_Model
from forms import EAVField

class EAV_AdminInline(admin.TabularInline):
    '''
    Базовый класс для встраиваемых форм редактирования элементов с EAV полями
    в списке полей формы обязательно должно быть EAV поле c именем fields_cache
    '''    
    
    def __init__(self, parent_model, admin_site):
        if 'fields_cache' not in self.fields:
            raise Exception('В списке отображаемых полей отсутствует fields_cache')
        
        return super(EAV_AdminInline, self).__init__(parent_model, admin_site)
    
    def get_eav_fields(self, obj):
        '''
        Функция, передающая список с доп. полями указанного обекта, пример:
        return obj.category.add_fields.all()
        '''
        raise Exception('Функция get_eav_fields должна быть переопределена наследником')
    
    def get_formset(self, request, obj=None, **kwargs):
        '''
        Хак заменяющий форму на специальную, в которой поле `fields_cache` меняется на EAV поле
        в зависимости от доп. полей категории объекта
        '''
        def eav_form_factory(obj):
            # Получаем список доп. полей категории указанного объекта
            add_fields = list( self.get_eav_fields(obj) )
            class EAVForm(forms.ModelForm):
                # Передаем список в конструктор EAV поля
                fields_cache = EAVField(add_fields, label=u'Доп. параметры', required=False)
                #TODO: сделать так, чтобы имя поля не было жестко указано и можно было внедрять нескольк EAV полей 
                
                class Meta:
                    model = self.model
            
            return EAVForm
        
        if obj and self.get_eav_fields(obj):
            # Если объект сохранен и указана его категория, то меняем формы
            self.form = eav_form_factory(obj)
            self.extra = 5
        else:
            # Иначе не показываем ни одной формы
            self.extra = 0
            
        return super(EAV_AdminInline, self).get_formset(request, obj, **kwargs)
      
#coding=utf-8
from django.db import models
from libs.modelfields import PickleField, JSONField
from django.utils.translation import ugettext as _
import forms


class EAV_Field(models.Field):
    def formfield(self, **kwargs):
        kwargs['form_class'] = forms.EAVField
        kwargs['widget'] = forms.EAVWidget
        return super(EAV_Field, self).formfield(**kwargs)    

class EAV_PickleField(PickleField, EAV_Field):
    pass
     
class EAV_JSONField(JSONField, EAV_Field):
    pass



registry = []
def register(model, parent_model=None, parent_attr='parent', sort_attr='sort', slug_attr='slug',
             name_attr='name', related_name='add_fields', ordering=None):
    '''
    '''

    if model in registry:
        raise Exception(
            _('The model %s has already been registered as EAV.') % model.__name__)
    registry.append(model)

    # Add options to the model's Options
    opts = model._meta
    opts.parent_attr= parent_attr
    opts.sort_attr  = sort_attr
    opts.slug_attr  = slug_attr
    opts.name_attr  = name_attr
    opts.ordering   = ordering or [parent_attr, sort_attr, 'id']
    opts.unique_together = ((parent_attr, slug_attr), )
    
    # Add fields if they do not exist
    for attr in [parent_attr, sort_attr, slug_attr, name_attr]:
        try:
            opts.get_field(attr)
        except models.FieldDoesNotExist:
            
            if attr==parent_attr:
                if not parent_model:
                    raise Exception(_('Parent model must be specified'))
                models.ForeignKey(
                                    parent_model, 
                                    verbose_name=_('Parent'),
                                    related_name=related_name, 
                                    blank=False
                                    ).contribute_to_class(model, attr)
            
            if attr==sort_attr:
                models.PositiveSmallIntegerField(
                                    _('Sort order'), 
                                    default=500, 
                                    null=True
                                    ).contribute_to_class(model, attr)
            
            if attr==slug_attr:
                models.SlugField(
                                    _('Slug'), 
                                    max_length=255, 
                                    blank=False
                                    ).contribute_to_class(model, attr)
            
            if attr==name_attr:
                models.CharField(
                                    _('Name'), 
                                    max_length=255, 
                                    blank=False
                                    ).contribute_to_class(model, attr)



class EAV_FieldsModel(models.Model):
    '''
    Базовый класс для модели, содержащий описания EAV полей,
    наследники данной модели должны обязательно содержать:
    
      - ForeignKey на модель к которой будут привязаны EAV поля, пример:
        category = models.ForeignKey(Category, blank=False) 
    
      - Порядок сортировки в Meta классе модели, пример:
        ordering = ['category', 'sort', 'id']
    
      - Иникальный индекс в Meta классе модели, пример:
        unique_together = ('category', 'slug')

    '''
    sort        = models.PositiveSmallIntegerField(u'Порядок сортировки', default=500, null=True) 
    slug        = models.SlugField(u'Код. имя', max_length=255, blank=False)
    name        = models.CharField(u'Название', max_length=50, blank=False)
   

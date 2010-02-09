#coding=utf-8
from django.db import models
from tinymce.models import HTMLField

#===========================================================================================
#
#            I N C L U D E
#
#===========================================================================================
        
class Includes(models.Model):
    '''
    Модель содержащая элементы каталог
    '''
    name        = models.CharField(u'Название', max_length=255)
    content     = HTMLField(u'Содержание')
    
    class Meta():
        verbose_name = u'включаемая область'
        verbose_name_plural = u'включаемые области'
            
    def __unicode__(self):       
        return unicode(self.name)
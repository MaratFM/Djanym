#coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail.fields import ImageWithThumbnailsField
from tinymce.models import HTMLField



#===========================================================================================
#
#            C O N S T A N T S
#
#===========================================================================================

OBJ_STATUS_HIDDEN = 0
OBJ_STATUS_PUBLIC = 1
OBJ_STATUS_ARCHIV = 2

OBJ_STATUS = (
    (OBJ_STATUS_HIDDEN, 'Скрыт'),
    (OBJ_STATUS_PUBLIC, 'Доступен'),
    (OBJ_STATUS_ARCHIV, 'В архиве'),
)  

#===========================================================================================
#
#            M O D E L S 
#
#===========================================================================================
class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().exclude(status=OBJ_STATUS_HIDDEN)
    

class Poll(models.Model):
    '''
    Модель для опросов
    '''
    
    status      = models.PositiveSmallIntegerField("Статус", choices=OBJ_STATUS, default=OBJ_STATUS_PUBLIC)
    question    = models.CharField("Вопрос", max_length=255)
    description = models.TextField("Описание", blank=True )
    pub_date    = models.DateField("Дата публикации", null=True, blank=True)
    
    objects = models.Manager()
    active = ActiveManager()
    def is_voted(self, request):
        return request.session.get('vote_%s' % self.id, False)            
    
    def votes_sum(self):
        from django.db.models import Sum, Max
        res = self.choice_set.aggregate(Sum('votes'),Max('votes'))
        return res

    def save(self, force_insert=False, force_update=False):
        from datetime import date
        if not self.pub_date:
            self.pub_date = date.today()
        super(Poll, self).save(force_insert, force_update) # Call the "real" save() method.

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        verbose_name = u'опрос'
        verbose_name_plural = u'опросы'
            
    def __unicode__(self):
        return self.question

   
    @models.permalink
    def get_absolute_url(self):
        return ('poll_detail', (), {'object_id': self.id} )


#===========================================================================================
#
#            M O D E L S 
#
#===========================================================================================
        
class Choice(models.Model):
    """
    Модель вариантов ответа
    """
    poll        = models.ForeignKey(Poll, null=False, blank=False, verbose_name='Опрос')
    choice      = models.CharField("Вариант ответа", max_length=255)
    sort        = models.PositiveSmallIntegerField("Порядок сортировки", default=500)
    votes       = models.PositiveIntegerField("Голосов", default=0)
    
    class Meta:
        unique_together = (("poll", "choice"),)        
        ordering = ['sort', 'id']
        verbose_name = u'вариант ответа'
        verbose_name_plural = u'варианты ответа'
            
    def __unicode__(self):
        return u'%s: %s' % (self.poll, self.choice)

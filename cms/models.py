#coding=utf-8
import mptt
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from sorl.thumbnail.fields import ImageWithThumbnailsField
from tinymce.models import HTMLField
from django.conf import settings


PAGE_TYPES = (
              (0, u'Статическая страница'),
              (1, u'Приложение'),
              (2, u'Перенаправление'),
              (3, u'Дубликат'),
              (4, u'Ссылка'),
              )

STATUS_HIDDEN = 0
STATUS_ACTIVE = 1
STATUS_CHOICES = (
    (0, 'Скрыт.'),
    (1, 'Активн.'),
)

class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(status=STATUS_ACTIVE)
#===========================================================================================
#
#            M O D E L S 
#
#===========================================================================================
class Page(models.Model):
    '''
    Модель для страниц сайта
    '''
    
    type        = models.PositiveSmallIntegerField(u'Тип страницы', blank=False, default=0, choices=PAGE_TYPES, editable=True)
    slug        = models.SlugField(u'Лат. написание', help_text=u'Должно быть уникальным среди страниц одного уровня', blank=True, max_length=40)#, unique_for_month="created")
    url         = models.CharField(u'URL', max_length=255, blank=True, editable=False)
    sort        = models.PositiveSmallIntegerField(u'Порядок сортировки', default=500) 

    name        = models.CharField(u'Название', help_text=u'Будет показано в меню, должно быть коротким: 1-2 слова', max_length=50)
    title       = models.CharField(u'Заголовок', help_text=u'Будет показано в заголовке страницы', max_length=255, blank=True)
    content     = HTMLField('Текст страницы', blank=True)
    link        = models.ForeignKey('self', blank=True, null=True, related_name='link_me', verbose_name=u'Ссылка/Дубликат:')
    app_url     = models.CharField(u'Приложение', max_length=255, blank=True, choices=settings.CMS_APPLICATIONS)

    parent      = models.ForeignKey('self', blank=True, null=True, related_name='children', verbose_name=u'Родитель')
    lft         = models.PositiveIntegerField(blank=True, null=True, editable=False)
    rght        = models.PositiveIntegerField(blank=True, null=True, editable=False)
    tree_id     = models.PositiveIntegerField(blank=True, null=True, editable=False)
    level       = models.PositiveIntegerField(blank=True, null=True, editable=False)

    status      = models.PositiveSmallIntegerField(u'Статус', choices=STATUS_CHOICES, default=STATUS_ACTIVE)    

    objects     = models.Manager()
    active_objects = ActiveManager()
    
    def save(self, force_insert=False, force_update=False): #, test_url=True):
        '''
        При сохранении добавляем к пути категориии путь её родителя,
        а также заполняем полное имя при его отсутствии
        '''
#        if not test_url:
#            return super(Page, self).save(force_insert, force_update)
        
        old_url = self.url
        
        if self.parent and self.parent.url:
            self.url = self.parent.url+'/'+self.slug
        else:
            self.url = self.slug

        if self.id and self.url!=old_url and self.get_descendant_count():
            
            repl = self.url +'/'
            old_len = len(old_url)+2 # для raw SQL 2 а для django 1
                
#            for p in self.get_descendants():
#                p.url = new_url +'/'+ p.url[old_len:]
#                p.save(test_url=False)

            from django.db import connection, transaction
            cursor = connection.cursor()
            cursor.execute('UPDATE '+self._meta.db_table+''' 
                            SET url = CONCAT(%s, SUBSTRING(url FROM %s)) 
                            WHERE tree_id = %s AND lft BETWEEN %s AND %s''', 
                           [repl, old_len, 
                            self.tree_id, self.lft, self.rght])
           
        self.title = self.title or self.name
        super(Page, self).save(force_insert, force_update)
        from middleware import init_menu
        init_menu()
        from django.core.urlresolvers import get_resolver
        get_resolver(None)
    
#    @models.permalink
    def get_absolute_url(self):
        if self.url:
            return  '/%s/' % self.url
        else:
            return '/'

    class Meta():
        ordering = ['tree_id', 'lft']
        verbose_name = u'страницу'
        verbose_name_plural = u'страницы'
            
    def __unicode__(self):       
        return u'%s %s' % ('--'*self.level,self.name)

mptt.register(Page, order_insertion_by=['sort', 'name'] )
    
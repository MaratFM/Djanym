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

OBJ_STATUS = (
    (OBJ_STATUS_HIDDEN, 'Не опубликован'),
    (OBJ_STATUS_PUBLIC, 'Опубликован'),
)  

#===========================================================================================
#
#            M O D E L S 
#
#===========================================================================================
def get_upload_path(instance, filename):
    import datetime
    if not instance.created:
        date = datetime.datetime.now()
    else:
        date = instance.created
    return 'img/%s/%s.%s' % (
                               date.strftime('%Y/%m/%d'),
                               instance.slug,
                               filename.rpartition('.')[2]
                               )        
        

class News(models.Model):
    '''
    Модель для новостей
    '''
    
    author      = models.ForeignKey(User, verbose_name="Автор", default = 1)
    slug        = models.SlugField('Лат. написание', help_text='Должно быть уникальным для своего дня публикации', blank=True, max_length=40)#, unique_for_month="created")

    name        = models.CharField("Название", max_length=255)
    anounce     = models.TextField("Анонс", blank=True )
    html        = HTMLField('HTML', blank=True)
    picture     = ImageWithThumbnailsField(u'Изображение', 
                                           max_length=255, 
                                           blank=True, 
                                           upload_to=get_upload_path,
                                           thumbnail={'size': (50, 50), 'options': ['crop']},
                                           extra_thumbnails={'large': {'size': (200, 300), 'options': []}}
                                           )    
#    source      = models.CharField("Источник информации", blank=True, max_length=255)
#    picture     = FileBrowseField("Изображение", max_length=200, initial_directory="/article/", extensions_allowed=['.jpg', '.jpeg', '.gif','.png','.tif','.tiff'], format='Image', blank=True, null=True)
#    picture     = ImageWithThumbnailsField("Изображение",  blank=True, upload_to=get_upload_path,
#                                           thumbnail={'size': (50, 50)},
#                                           extra_thumbnails={
#                                                             'icon': {'size': (16, 16), 'options': ['crop', 'upscale']},
#                                                             'large': {'size': (200, 400)},
#                                                             },
#                                            )
#    picture     = StdImageField("Изображение",  blank=True, upload_to=get_upload_path,
#                                size=(640, 480), thumbnail_size=(100, 100, True)) # all previous features in one declara
    
    absolute_url    = models.CharField("Url", editable=False, blank=True, max_length=255)
    
    status      = models.PositiveSmallIntegerField("Статус объекта", choices=OBJ_STATUS, default=OBJ_STATUS_HIDDEN)

    created     = models.DateTimeField("Дата создания объекта", auto_now_add=True)
    updated     = models.DateTimeField("Дата обновления объекта", auto_now=True)
    pub_date    = models.DateTimeField("Дата публикации", blank=True, null=True)

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
            
    def __unicode__(self):
        return self.name

   
    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {'object_id': self.id} )

    def save(self, force_insert=False, force_update=False):
        from django.utils.html import strip_tags, clean_html
        from django.utils.text import truncate_words
        
        self.html = clean_html(self.html)
        if not self.anounce and self.html:
            self.anounce = truncate_words(strip_tags(self.html), 100)
        
        super(News, self).save(force_insert, force_update) # Call the "real" save() method.

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
       
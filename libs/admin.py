#coding=utf-8
from sorl.thumbnail.main import DjangoThumbnail

def thumbnail(image_path, size=(50,50), options=['crop']):
    '''
    Поле в админке с уменьшенным изображением
    '''
    if image_path:
        try:
            thumbnail = DjangoThumbnail(image_path, size, options)
        except ValueError: 
            return ''
        return '<img src="%s" width="%s" height="%s" />' % (str(thumbnail.absolute_url), thumbnail.width(), thumbnail.height() )
    else:
        return ''      

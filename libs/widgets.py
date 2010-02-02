#coding=utf-8
       
import os
from django import forms
from django.conf import settings
from django import template
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode

class HTML(forms.Widget):

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = force_unicode(value)
        return mark_safe(u'%s' % value)

class TinyMCE(forms.Textarea):

    class Media:
        js = (
            'static/tiny_mce/tiny_mce.js',
        )

    def render(self, name, value, attrs=None):
        rendered = super(TinyMCE, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
tinyMCE.init({
    language : "ru", // change language here 
    mode : "exact",
    elements : "id_%s",
    theme : "advanced",
//   skin : "o2k7",
//   skin_variant : "silver",

    plugins : "fullscreen,searchreplace,contextmenu,paste,table", //safari,spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,imagemanager,filemanager",
    theme_advanced_buttons1 : "cut,copy,paste,pastetext,pasteword,|,cleanup,removeformat,|,undo,redo,|,search,replace,|,link,unlink,anchor,image,code,|,tablecontrols",
    theme_advanced_buttons2 : "fullscreen,formatselect,fontsizeselect,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,outdent,indent,|,forecolor,backcolor",
    theme_advanced_buttons3 : "",

//    theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
//    theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
//    theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
//    theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",

    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resize_horizontal : false,
    theme_advanced_resizing : true

});
</script>
''' % (name))
        
        
class AdminThumbWidget(forms.FileInput):
    """
    A Image FileField Widget that shows a thumbnail if it has one.
    """
    def __init__(self, attrs={}):
        super(AdminThumbWidget, self).__init__(attrs)
 
    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            try:
                from sorl.thumbnail.main import DjangoThumbnail
                thumb = '<img src="%s" align="absmiddle">' % DjangoThumbnail(value.name, (50,500), []).absolute_url
            except:
                # just act like a normal file
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' %
                    (_('Currently:'), value.url, os.path.basename(value.path), _('Change:')))
            else:
                output.append('<a class="thumb" target="_blank" href="%s">%s</a> %s ' %
                    (value.url, thumb, _('Change:')))
        output.append(super(AdminThumbWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))        
        

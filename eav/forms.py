#coding=utf-8
from django import forms


class EAVWidget(forms.widgets.MultiWidget):
    '''
    Виджет для отображения EAV полей, в параметре attrs конструктора виджета 
    можно передать параметры шаблона отображения:
        - prefix - html код предшествующий списку полей
        - template - шаблон доп. поля, должен содержать именованые параметры: %(label)s и %(widget)s
        - postfix - html код завершающий список полей
    
    '''
    default_attrs = {
                     'prefix': '<table><tr>',
                     'template': '<td style="padding:0 4px 0 0; border:0;"><label style="white-space: nowrap;">%(label)s:&nbsp;%(widget)s</label></td>',
                     'postfix': '</tr></table>',
                     }
    
    def __init__(self, add_fields=None, attrs={}):
        self.add_fields = add_fields or []
        attrs['style'] = 'width: 5em;'
        self.default_attrs.update(attrs)
        widgets = [forms.widgets.TextInput(attrs=attrs) for i in xrange(len(self.add_fields))]
        super(EAVWidget, self).__init__(widgets, attrs)

    def format_output(self, rendered_widgets):
        '''
        Форматируем вывод списка доп. полей
        '''
        if self.add_fields:
            out = []
            out.append(self.default_attrs['prefix'])
            for i, w in enumerate(rendered_widgets):
                out.append(self.default_attrs['template'] % 
                           {'label': self.add_fields[i].name,  'widget': w} 
                           )
            out.append(self.default_attrs['postfix'])
        else:
            out = rendered_widgets
        return u''.join(out)
    
    def decompress(self, value):
        '''
        Преобразовывает данные из словаря, сохраненного в EAV поле модели, в массив
        значений, который будет отображен в полях формы
        '''        
        try:
            out = []
            for f in self.add_fields:
                out.append(value.get(f.slug, ''))
            return out
        except:
            return [None]*len(self.add_fields)



class EAVField(forms.fields.MultiValueField):
    '''
    Поле формы для отображения EAV поля модели
    '''
    widget  = EAVWidget
    
    def __init__(self, add_fields=None, *args, **kwargs):
        '''
        Получаем список доп. полей, добавляем текстовые поля и передаем список доп. полей виджету
        '''
        self.add_fields = add_fields or []
        if self.add_fields:
            fields = [forms.fields.CharField(required=False) for i in xrange(len(add_fields))]
            self.widget = self.widget(add_fields)
        else:
            fields = []
        super(EAVField, self).__init__(fields, *args, **kwargs)
    
    def compress(self, data_list):
        '''
        Преобразовывает данные полученные из формы (массив data_list) в словарь
        который будет записан в EAV поле модели
        '''
        out = {}
        for i,f in enumerate(self.add_fields):
            try:
                out[f.slug] = data_list[i] #.strip()
            except IndexError:
                out[f.slug] = ''

        return out      



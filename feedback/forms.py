#coding=utf-8
from django import forms

class FeedbackForm(forms.Form):
    '''
    Форма обратной связи
    '''
    name        = forms.CharField(label=u"ФИО", required=True, widget=forms.TextInput(attrs={'class':'req', 'size': '5'}))
    phone       = forms.CharField(label=u"Телефон", required=True, widget=forms.TextInput(attrs={'class':'req req-phone', 'size': '5'}))
    email       = forms.EmailField(label=u"E-mail", required=False, widget=forms.TextInput(attrs={'class':'req req-email', 'size': '5'}))
    message     = forms.CharField(label=u"Вопрос", required=True, widget=forms.Textarea(attrs={'cols':'5', 'rows':'5'}))
  

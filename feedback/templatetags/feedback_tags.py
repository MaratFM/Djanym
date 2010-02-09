#coding=utf-8
from django import template
from feedback.forms import FeedbackForm
from django.shortcuts import render_to_response
register = template.Library()


@register.inclusion_tag('feedback/form.html')
def render_feedback():
    '''
    Тэг для вывода списка категорий
    '''
    return {
            'form': FeedbackForm(),
            }

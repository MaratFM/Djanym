import datetime
from django import template
from news.models import News, OBJ_STATUS_PUBLIC

register = template.Library()

@register.inclusion_tag('news/latest_snippet.html')
def render_latest_news(num):
    entries = News.objects.filter(status=OBJ_STATUS_PUBLIC)[:num]
    return {
            'object_list': entries,
            }

@register.inclusion_tag('news/month_links_snippet.html')
def render_month_links():
    return {
            'dates': News.objects.dates('pub_date', 'month'),
            }
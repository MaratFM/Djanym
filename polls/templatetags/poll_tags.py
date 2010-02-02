import datetime
from django import template
from polls.models import Poll, OBJ_STATUS_PUBLIC
from django.core.cache import cache

register = template.Library()

@register.inclusion_tag('polls/latest_snippet.html')
def render_latest_poll(request):
    object, agregators, choices = cache.get('latest_poll_object') or (None,None,None)    
    if not object:
        object = Poll.active.filter(status=OBJ_STATUS_PUBLIC).select_related()[0]
        agregators = object.votes_sum()
        choices = object.choice_set.all()
        cache.set('latest_poll_object', (object, agregators, choices))
    print object.is_voted(request)
    return {
            'request': request,
            'object': object,
            'agregators': agregators,
            'choices': choices,
            'is_voted': object.is_voted(request),
            }


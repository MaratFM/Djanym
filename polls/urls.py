#coding=utf-8

from django.conf.urls.defaults import *
from views import *
from models import Poll

info_dict = {
    'queryset': Poll.active.all(),
}

urlpatterns = patterns('',
    (r'^$',                         'django.views.generic.list_detail.object_list', 
                                    dict(info_dict, paginate_by=10), 
                                    'polls_index'),
    url(r'^(?P<object_id>\d+)/$',   detail, 
                                    name='poll_detail'),
    url(r'^(?P<object_id>\d+)/results/$', 
                                    'django.views.generic.list_detail.object_detail', 
                                    dict(info_dict, template_name='polls/results.html'), 
                                    'poll_results'),
    url(r'^(?P<object_id>\d+)/vote/$', 
                                    vote,
                                    name='poll_vote'),
)




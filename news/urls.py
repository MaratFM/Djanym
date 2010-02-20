#coding=utf-8

from django.conf.urls.defaults import *
from views import *
from models import News

news_list_dict = {'queryset': News.objects.all(),
                  'paginate_by': 10,
                  }
news_detail_dict = {'queryset': News.objects.all(),
                    }

urlpatterns = patterns('',
   url(r'^$', 
       'django.views.generic.list_detail.object_list', 
       news_list_dict, 
       name='news_list' ),
   url(r'^(?P<object_id>\d+)/$', 
       'django.views.generic.list_detail.object_detail', 
       news_detail_dict, 
       name='news_detail'),
)




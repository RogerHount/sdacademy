from django.conf.urls import patterns, include, url
from students.views import detail, list_view


urlpatterns = patterns('',
	url(r'^$', list_view, name='list_view'),
    url(r'^(?P<id_of_student>\d+)/$', detail, name='detail'),
)

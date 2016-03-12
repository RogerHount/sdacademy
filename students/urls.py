from django.conf.urls import patterns, include, url
from students.views import detail, list_view, create, edit, remove


urlpatterns = patterns('',
	url(r'^$', list_view, name='list_view'),
    url(r'^(?P<id_of_student>\d+)/$', detail, name='detail'),
    url(r'^add/$', create, name='add'),
    url(r'^edit/(?P<student_to_edit>\d+)$', edit, name='edit'),
    url(r'^remove/(?P<student_to_remove>\d+)$', remove, name='remove'),
)

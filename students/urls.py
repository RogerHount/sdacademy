from django.conf.urls import patterns, include, url
from students.views import StudentDetailView, StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView
#from students.views import detail, list_view, create, edit, remove


urlpatterns = patterns('',
	url(r'^$', StudentListView.as_view(), name='list_view'),
#	url(r'^$', list_view, name='list_view'),
	url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='detail'),
#	url(r'^(?P<pk>\d+)/$', detail, name='detail'),
	url(r'^add/$', StudentCreateView.as_view(), name='add'),
#	url(r'^add/$', create, name='add'),
	url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='edit'),
#	url(r'^edit/(?P<student_to_edit>\d+)/$', edit, name='edit'),
	url(r'^remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='remove'),
)

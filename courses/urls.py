from django.conf.urls import patterns, include, url
from courses.models import Course
from courses.views import detail, add, edit, remove, add_lesson


urlpatterns = patterns('',
    url(r'^(?P<id_of_course>\d+)/$', detail, name='detail'),
    url(r'^add/$', add, name='add'),
    url(r'^edit/(?P<id_of_course>\d+)/$', edit, name='edit'),
    url(r'^remove/(?P<id_of_course>\d+)/$', remove, name='remove'),
    url(r'^(?P<id_of_course>\d+)/add-lesson$', add_lesson, name='add_lesson'),
)

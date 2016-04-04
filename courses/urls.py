from django.conf.urls import patterns, include, url
from courses.models import Course
from courses.views import add_lesson
from courses.views import CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<id_of_course>\d+)/add_lesson$', add_lesson, name='add-lesson'),
)

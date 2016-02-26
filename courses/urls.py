from django.conf.urls import patterns, include, url
from courses.models import Course
from courses.views import detail


urlpatterns = patterns('',
    url(r'^(?P<id_of_course>\d+)/$', detail, name='detail' ),
)

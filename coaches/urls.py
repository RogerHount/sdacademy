from django.conf.urls import patterns, include, url
from coaches.views import detail


urlpatterns = patterns('',
    url(r'^(?P<id_of_coach>\d+)/$', detail, name='detail'),
)

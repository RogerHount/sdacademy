from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

    url('^$', "sdacademy.views.index", name='index'),
    url('^contact/', 'sdacademy.views.contact' , name='contact'),
    url('^student_list/', 'sdacademy.views.student_list', name='student_list'),
    url('^student_detail/', 'sdacademy.views.student_detail', name='student_detail'),
)
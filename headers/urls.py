from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_project_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'headers.views.headers', name='headers'),
)

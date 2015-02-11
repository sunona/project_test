from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'headers.views.headers', name='headers'),
)

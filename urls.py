from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('testapp.views',
    url('^$', 'index'),
    url('^create/$', 'create'),
    url('^edit/(?P<pk>\d+)/$', 'update'),
)

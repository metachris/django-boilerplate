from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^project/(?P<project_id>\d+)/$', 'helloworldapp.views.project', name="xx"),
    url(r'^$', 'helloworldapp.views.home', name='home'),
)


urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

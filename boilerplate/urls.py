from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'helloworldapp.views.home', name='home'),
    url(r'^project/(?P<project_id>\d+)/$', 'helloworldapp.views.project'),

    # Login and logout url's
    (r'^login/$', 'django.contrib.auth.views.login',
         {'template_name': 'login.html'}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
         {'template_name': 'login.html'}),
    url(r'^register/$', 'main.views.register'),
    url(r'^logout/$', 'main.views.logout'),

    # Admin Url's
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

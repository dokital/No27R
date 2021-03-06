from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'No27R.views.home', name='home'),
    # url(r'^No27R/', include('No27R.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #homepage
    url(r'^$', 'blog.views.getPosts'),
    url(r'^(?P<selected_page>\d+)/?$', 'blog.views.getPosts'),
)

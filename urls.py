from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
import hello_world.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jjhecdriverschool.views.home', name='home'),
    url(r'^hello/', include(hello_world.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

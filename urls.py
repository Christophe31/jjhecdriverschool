from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
import hello_world.urls
import crm.urls
import profile.urls
import trainer.urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/', include(hello_world.urls)),
    url(r'^crm/', include(crm.urls)),
    url(r'^profile/', include(profile.urls)),
    url(r'^trainer/', include(trainer.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include(hello_world.urls))
    # Uncomment the next line to enable the admin:
)

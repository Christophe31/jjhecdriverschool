from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
import hello_world.urls
import crm.urls
import profile.urls
import trainer.urls
from django.contrib import admin
admin.autodiscover()

# ... the rest of your URLconf goes here ...

urlpatterns = patterns('',
    # index page
    url(r'^$', include(hello_world.urls)),
    # local apps routing
    url(r'^hello/', include(hello_world.urls)),
    url(r'^crm/', include(crm.urls)),
    url(r'^profile/', include(profile.urls)),
    url(r'^trainer/', include(trainer.urls)),
    # external module routing
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
              'document_root': settings.MEDIA_ROOT,
               }),
    )

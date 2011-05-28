from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
import hello_world.urls
import crm.urls
import profile.urls
import trainer.urls
from lbforum.accountviews import profile as lbprofile

import jqmobile
from django.contrib import admin
admin.autodiscover()
jqmobile.autodiscover()

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
    url(r'^ma/', include(jqmobile.site.urls)),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'lbforum/',include('lbforum.urls')),
    url(r'^user/(?P<user_id>\d+)/$', lbprofile, name='user_profile'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
              'document_root': settings.MEDIA_ROOT,
               }),
    )
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    from mobileadmin.conf import settings as masettings

    urlpatterns += patterns('django.views.static',
        (masettings.MEDIA_REGEX, 'serve', {'document_root': masettings.MEDIA_PATH}),
    )

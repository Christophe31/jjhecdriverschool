from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
import home.urls
import crm.urls
import profile.urls
import trainer.urls

import jqmobile
from django.contrib import admin
admin.autodiscover()
jqmobile.autodiscover()


urlpatterns = patterns('',
    # index page
    url(r'^$', include(home.urls)),
    # favicon
    url(r'^favicon\.ico$','django.views.generic.simple.redirect_to', {'url': settings.MEDIA_URL+'favicon.ico'}),
    # local apps routing
    url(r'^crm/', include(crm.urls)),
    url(r'^profile/', include(profile.urls)),
    url(r'^trainer/', include(trainer.urls)),
    # external module routing
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ma/', include(jqmobile.site.urls)),
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
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

#######
# Forum
#######
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings
from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({
                    'form_class': RegistrationFormUtfUsername
        })

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^forum/pm/', include('messages.urls'))
    )

urlpatterns += patterns('',
    url(r'^forum/account/', include(authopenid_urlpatterns)),
    url(r'^forum/', include('djangobb_forum.urls', namespace='djangobb')),
)

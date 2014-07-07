from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    url(r'^countries/$', 'signups.views.countries', name='countries'),
    url(r'^players/$', 'signups.views.players', name='players'),
    url(r'^matches/$', 'signups.views.matches', name='matches'),    
    #countries
    url(r'^countries/brazil/$', 'signups.views.brazil', name='brazil'),
    url(r'^countries/argentina/$', 'signups.views.argentina', name='argentina'),
    url(r'^countries/germany/$', 'signups.views.germany', name='germany'),    
    #players
    url(r'^players/messi/$', 'signups.views.messi', name='messi'),    
    url(r'^players/neymar/$', 'signups.views.neymar', name='neymar'),    
    url(r'^players/muller/$', 'signups.views.muller', name='muller'),
    #matchess
    url(r'^matches/arg_ned/$', 'signups.views.arg_ned', name='arg_ned'),    
    url(r'^matches/ger_usa/$', 'signups.views.ger_usa', name='ger_usa'),    
    url(r'^matches/bra_ger/$', 'signups.views.bra_ger', name='bra_ger'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
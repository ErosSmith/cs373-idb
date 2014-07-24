from django.conf.urls import patterns, include, url
from django.conf import settings
from wc_app import views

from django.contrib import admin
from wc_app.api import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'world_cup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),


    #this is the parent countries url
    url(r'^countries/$', views.countries, name='countries'),
    #this one is a for a specfic country
    url(r'^countries/(?P<c_name>\w+)/$', views.country, name='country'), 
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<p_name>[\w]+)/$', views.player, name='player'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^matches/(\d+)/$', views.match, name='match'),
    url(r'^test/$', views.test, name='test'),

    #RESTful API
    url(r'^api/', include(CountryResource().urls)),
    url(r'^api/', include(PlayerResource().urls)),
    url(r'^api/', include(MatchResource().urls)),
)

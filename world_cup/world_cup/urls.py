from django.conf.urls import patterns, include, url
from django.conf import settings
from wc_app import views

from django.contrib import admin
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
    url(r'^countries/(\d+)/$', views.country, name='country'), 
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(\d+)/$', views.player, name='player'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^matches/(\d+)/$', views.match, name='match'),
    url(r'^test/$', views.test, name='test'),
)

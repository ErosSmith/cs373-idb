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
    url(r'^countries/(\d+)/$', views.country, name='country'),
    url(r'^player/(\d+)/$', views.player, name='player'),
    url(r'^countries/$', views.countries, name='countries'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^matches/(\d+)/$', views.match, name='match'),
)

from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from untitled.views import *

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^untitled/', include('untitled.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/', catch_page_info),
    # url(r'^holiday/', day_type),
    url(r'^day_count/', day_count),
    url(r'^test_kuaidi/', test_kuaidi),
    url(r'^test_webapi/', test_webapi),
    url(r'^test_jsapi/', test_jsapi),
    url(r'^test_map/', test_map),
)

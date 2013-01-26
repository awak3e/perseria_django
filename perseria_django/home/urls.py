from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Perseria.views.home', name='home'),
    # url(r'^Perseria/', include('Perseria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'home.views.index'),
    url(r'^auth/', 'home.views.auth'),
    url(r'^signout/', 'home.views.signout'),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bookmapsapp.views.bookmap', name = 'bookmap'),
    url(r'^get_data/', 'bookmapsapp.views.get_data', name='get_data'),
    url(r'^add_book/', 'bookmapsapp.views.add_book', name='add_book'),
)

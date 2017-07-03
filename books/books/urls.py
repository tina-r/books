from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^buecher/$', 'booklist.views.buecher'),
    url(r'^buecher/titel_liste/', include('booklist.urls')),
]

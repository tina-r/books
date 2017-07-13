from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^buecher/$', 'booklist.views.buecher'),
    url(r'^buecher/sign_in/$', 'booklist.views.signup', name='signup'),
    #url(r'^buecher/log_in/$', 'booklist.views.login', name='login'),
    url(r'^buecher/log_in/$', auth_views.login, name='login'),
    url(r'^buecher/log_out/$', auth_views.logout, name='logout'),
    url(r'^buecher/titel_liste/$', 'booklist.views.list_titles'),
    url(r'^buecher/titel_liste/renew/$', 'booklist.views.renew_book'),
    url(r'^buecher/titel_liste/content_list/$', 'booklist.views.list_content'),
    url(r'^buecher/titel_liste/(?P<pk>\d+)/$', 'booklist.views.edit_book'),
    url(r'^buecher/titel_liste/delete_list/$', 'booklist.views.list_delete_titles'),
    url(r'^buecher/titel_liste/delete_list/(?P<pk>\d+)/$', 'booklist.views.delete_book'),
]


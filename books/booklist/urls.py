from django.conf.urls import patterns, include, url

urlpatterns = patterns('booklist.views',
    (r'^$', 'list_titles'),
)

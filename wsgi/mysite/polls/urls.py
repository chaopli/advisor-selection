from django.conf.urls import patterns, url
from django.conf import settings

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.loginpage),
    url(r'^login$', views.loginpage, name='loginpage'),
    url(r'^logout$', views.logoutView),
    url(r'^select-(?P<advisor>[\w.@+-]+)$', views.select),
    url(r'^reselect$', views.reselect),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                             { 'document_root': settings.MEDIA_ROOT}))

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.loginpage, name='loginpage'),
    url(r'^logout$', views.logoutView, name='loginpage'),
]

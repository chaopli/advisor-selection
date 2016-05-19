from django.conf.urls import  url


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

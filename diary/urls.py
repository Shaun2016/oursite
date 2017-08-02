from django.conf.urls import url

from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^$', views.to_login, name='to_login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
]
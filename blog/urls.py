from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^monday/$',views.monday_list, name='monday_list'),
    #url(r'^shows/new/$', views.show_new, name='show_new'),
    #url(r'^shows/(?P<pk>[0-9]+)/edit/$', views.show_edit, name='show_edit'),
]

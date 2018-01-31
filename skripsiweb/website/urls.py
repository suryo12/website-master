from django.conf.urls import url
from . import views
from .views import APINodeView, get_data_show


app_name = 'skripsiweb'

urlpatterns = [
    url(r'^$', views.)
    #url(r'^$', views.get_data_show, name='home'),
    #url(r'^api/$', APINodeView.as_view(), name='APINodeView'),
    #url(r'^(?P<nodeid_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<nodeid_id>[0-9]+)/$', views.detail, name='detail'),
]
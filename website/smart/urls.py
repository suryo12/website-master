from django.conf.urls import url
from . import views
from .views import APINodeView, ChartCoba

urlpatterns = [
    # /smart/
    url(r'^$', views.IndexView, name='index'),
    url(r'^$', views.ChartCoba, name='chart'),

    # /smart/<node_id>/
    url(r'^(?P<node_id>[0-9]+)/$', views.DetailView, name='detail'),
    url(r'^(?P<node_id>[0-9]+)/(?P<tahun>[0-9]+)/(?P<bulan>[0-9]+)/(?P<hari>[0-9]+)/$', views.ChartDetail, name='chartdetail'),
    url(r'^api/$', APINodeView.as_view(), name='APINodeView'),


]
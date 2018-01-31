from django.conf.urls import url
from . import views
from .views import APINodeView, HomeView, get_data, ChartData

app_name = 'landslide'

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^api/$', APINodeView.as_view(), name='APINodeView'),
    url(r'^(?P<nodeid_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
#    url(r'^api/data/$', get_data2, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]
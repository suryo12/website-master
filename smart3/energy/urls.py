from django.conf.urls import url
from . import views
#from .views import ListEnergyView

urlpatterns = [
     #url(r'^$', ListEnergyView.as_view(), name='ListEnergyView'),
    #/energy/
    url(r'^$', views.index, name='index'),

    #/energy/sekian/
    url(r'^(?P<Node_ID>[1001-1003]+)/$', views.detail, name='detail'),
]
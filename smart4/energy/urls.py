from django.conf.urls import url
from . import views
#from .views import ListEnergyView

urlpatterns = [
     #url(r'^$', ListEnergyView.as_view(), name='ListEnergyView'),
    #/energy/
    url(r'^$', views.index, name='index'),

    #/energy/sekian/
    url(r'^(?P<node_id>[1-10]+)/$', views.detail, name='detail'),
]
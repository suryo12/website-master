from django.conf.urls import url
from .views import ListEnergyView #APIEnergyView

urlpatterns = [
    url(r'^$', ListEnergyView.as_view(), name='ListEnergyView'),
]

from .views import HomeView, get_data, ChartData
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^energy/', include('energy.urls')),
    url(r'^admin/', admin.site.urls),
]
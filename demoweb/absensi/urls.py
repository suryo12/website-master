from django.conf.urls import url
from .views import ListAttendanceView,APIAttendanceView

urlpatterns = [
    url(r'^$', ListAttendanceView.as_view(), name='ListAttendanceView'),
    url(r'^api/$', APIAttendanceView.as_view(), name='APIAttendanceView'),
]

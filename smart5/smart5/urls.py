from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^energy/', include('energy.urls',namespace='energy')),
    url(r'^admin/', admin.site.urls),
]


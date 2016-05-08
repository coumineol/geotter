from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('lctst.apps.app1.urls')),
    url(r'^julia/', include('lctst.apps.app2.urls')),
]
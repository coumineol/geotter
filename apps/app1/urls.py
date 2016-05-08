from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView
from lctst.apps.app1.views import RedirectToGeo, LocationCreateViewDetect, GeoMainView, LocationCreateViewCity, \
                                  LocationCreateViewCountry, register_view

urlpatterns = [
    url(r'^$', GeoMainView.as_view(template_name="app1/index.html")),
    url(r'^login/$', auth_views.login, {'template_name': 'app1/login.html'}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}),  # !!!
    url(r'^register/$', TemplateView.as_view(template_name='app1/register.html')),
    url(r'^registered/$', register_view),
    url(r'^redirect/$', RedirectToGeo.as_view()),
    url(r'^geo/$', GeoMainView.as_view()),
    url(r'^geo/create/detect/$', LocationCreateViewDetect.as_view()),
    url(r'^geo/create/city/$', LocationCreateViewCity.as_view()),
    url(r'^geo/create/country/$', LocationCreateViewCountry.as_view()),
]
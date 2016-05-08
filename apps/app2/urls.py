from django.conf.urls import url
from lctst.apps.app2.views import JuliaView, UserFollowerCreateView

urlpatterns = [
    url(r'^$', JuliaView.as_view()),
    url(r'^create/', UserFollowerCreateView.as_view()),
]
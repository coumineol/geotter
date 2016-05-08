from django.views.generic.base import RedirectView
from django.views.generic import ListView
from django.views.generic.edit import BaseCreateView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponsePermanentRedirect
from lctst.apps.app1.models import Location
import datetime
import requests


class RedirectToGeo(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            self.url = '/geo/'
        else:
            self.url = '/login/'

        return super(RedirectToGeo, self).get_redirect_url(*args, **kwargs)


class GeoMainView(ListView):

    model = Location
    template_name = "app1/geo.html"

    def get_queryset(self):
        username = None
        if self.request.user.is_authenticated():
            active_user = self.request.user
            queryset = Location.objects.filter(user=active_user).order_by('date')
            return queryset
        else:
            return None


class LocationCreateViewDetect(BaseCreateView):

    model = Location
    fields = ['latitude', 'longitude']
    success_url = '/geo/'

    def form_valid(self, form):
        active_user = self.request.user
        form.instance.user = active_user
        form.instance.date = datetime.datetime.now()
        response = super(LocationCreateViewDetect, self).form_valid(form)
        return response

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class LocationCreateViewCity(BaseCreateView):

    model = Location
    fields = []
    success_url = '/geo/'

    def get_lat_lon(self):
        city = self.request.POST["getCity"]
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + city + "&sensor=false"
        response = requests.get(url)
        resp_json = response.json()
        latitude = resp_json['results'][0]['geometry']['location']['lat']
        longitude = resp_json['results'][0]['geometry']['location']['lng']
        return latitude, longitude

    def form_valid(self, form):
        latitude, longitude = self.get_lat_lon()
        active_user = self.request.user
        form.instance.user = active_user
        date = datetime.datetime.now()
        form.instance.date = date
        form.instance.latitude = latitude
        form.instance.longitude = longitude
        response = super(LocationCreateViewCity, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'date': date,
                'latitude': latitude,
                'longitude': longitude,
            }
            return JsonResponse(data)
        else:
            return response

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class LocationCreateViewCountry(BaseCreateView):

    model = Location
    fields = []
    success_url = '/geo/'

    def get_lat_lon(self):
        country = self.request.POST["getCountry"]
        zip = self.request.POST["getZip"]
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + country + "%20" + zip + "&sensor=false"
        response = requests.get(url)
        resp_json = response.json()
        latitude = resp_json['results'][0]['geometry']['location']['lat']
        longitude = resp_json['results'][0]['geometry']['location']['lng']
        return latitude, longitude

    def form_valid(self, form):
        latitude, longitude = self.get_lat_lon()
        active_user = self.request.user
        form.instance.user = active_user
        date = datetime.datetime.now()
        form.instance.date = date
        form.instance.latitude = latitude
        form.instance.longitude = longitude
        response = super(LocationCreateViewCountry, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'date': date,
                'latitude': latitude,
                'longitude': longitude,
            }
            return JsonResponse(data)
        else:
            return response

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


def register_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.create_user(username=username, password=password)
    user.save()

    return HttpResponsePermanentRedirect("/login/")
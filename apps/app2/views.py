from django.views.generic.base import View, TemplateView
from django.views.generic import ListView
from django.http import HttpResponse
from lctst.apps.app2.models import TwitterUser, TwitterFollower
from lctst.apps.app2 import twitapi
from lctst.apps.app2.tasks import Retweet_periodic


class JuliaView(ListView):

    model = TwitterFollower
    template_name = "app2/julia.html"

    def get_context_data(self, **kwargs):

        context = super(JuliaView, self).get_context_data(**kwargs)

        return context


class UserFollowerCreateView(View):

    def post(self, request, *args, **kwargs):

        username = request.POST['username']

        num_results = TwitterUser.objects.filter(username=username).count()

        if num_results == 0:

            u = TwitterUser(username=username)
            u.save()

            try:
                task = Retweet_periodic()
                task.delay(username)
            except:
                pass

            followers = twitapi.followers(username)

            for follower, count in followers.items():
                f = TwitterFollower(username=follower, followercount=count)
                f.followed = TwitterUser.objects.get(username=username)
                f.save()

        return HttpResponse("")
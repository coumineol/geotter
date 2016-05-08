from django.contrib import admin
from lctst.apps.app2.models import TwitterUser, TwitterFollower, TaskHistory


admin.site.register(TwitterUser)
admin.site.register(TwitterFollower)
admin.site.register(TaskHistory)

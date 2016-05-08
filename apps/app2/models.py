from django.db import models
from django.utils.translation import ugettext_lazy as _
import jsonfield


class TwitterUser(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default='0')

    def __str__(self):
        return str(self.id)


class TwitterFollower(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default='0')
    followed = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='followed_user')
    followercount = models.IntegerField()

    def __str__(self):
        return str(self.id)


class TaskHistory(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name=_("Task name"),
        help_text=_("Select a task to record"),
        )

    history = jsonfield.JSONField(
        default={},
        verbose_name=_("history"),
        help_text=_("JSON containing the tasks history")
        )

    class Meta:
        verbose_name = _('Task History')
        verbose_name_plural = _('Task Histories')

    def __unicode__(self):
        return _("Task History of Task: %s") % self.name
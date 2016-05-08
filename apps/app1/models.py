from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='location_user')
    date = models.DateTimeField()
    latitude = models.TextField(max_length=10, default='0')
    longitude = models.TextField(max_length=10, default='0')

    def __str__(self):
        return str(self.id)
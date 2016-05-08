from __future__ import absolute_import
from celery.task import PeriodicTask
from celery import Celery
from lctst.apps.app2.twitapi import tweetit, retweet
from datetime import timedelta, datetime
from celery.utils.log import get_task_logger
from lctst.apps.app2.models import TaskHistory


logger = get_task_logger(__name__)

app = Celery('myApp')


class Retweet_periodic(PeriodicTask):

    run_every = timedelta(hours=12)

    def run(self, screen_name, **kwargs):

        logger.info("Start task")
        now = datetime.now()
        date_now = now.strftime("%d-%m-%Y %H:%M:%S")

        retweet(screen_name)

        name = "retweet_periodic"
        taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
        taskhistory.save()
        logger.info("Task finished")


class Tweet_periodic(PeriodicTask):

    run_every = timedelta(days=3)

    def run(self, **kwargs):

        logger.info("Start task")
        now = datetime.now()
        date_now = now.strftime("%d-%m-%Y %H:%M:%S")

        try:
            tweet_body = "Time for some Java livestreams: https://www.livecoding.tv/username1, https://www.livecoding.tv/username2"
            tweetit(tweet_body)
        except:
            pass


        name = "tweet_periodic"
        taskhistory = TaskHistory.objects.get_or_create(name=name)[0]
        taskhistory.save()
        logger.info("Task finished")
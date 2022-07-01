import os
from celery import Celery

from celery.schedules import crontab
import mysite.tasks

#
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

#
import django
django.setup()

app = Celery("mysite")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()



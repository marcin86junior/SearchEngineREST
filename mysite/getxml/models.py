from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=50, blank=True, null=True)
    guid = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50)
    pubDate = models.CharField(max_length=50)

    def __str__(self):
        return self.title

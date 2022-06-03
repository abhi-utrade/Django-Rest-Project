from django.db import models
from django.contrib.auth.models import User


class WatchList(models.Model):
    user = models.CharField(max_length=200)
    watchlist = models.CharField(max_length=200, default='AAP')

    def __str__(self):
        return self.watchlist



import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import caching.base


HASH_CHOICES = (
    (0, "MD5"),
    (1, "SHA1"),
    (2, "SHA256"),
    (3, "Git Tag"),
    )


"""
class UserProfile(caching.base.CachingMixin, models.Model):
    objects = caching.base.CachingManager()

    user = models.OneToOneField(User)
    date_created = models.DateTimeField('date created', auto_now_add=True)

    # Other fields here
    accepted_eula = models.BooleanField()

    def __unicode__(self):
        return "<UserProfile(%s)>" % self.user


class Project(caching.base.CachingMixin, models.Model):
    objects = caching.base.CachingManager()

    user = models.OneToOneField(User)
    date_created = models.DateTimeField('date created', auto_now_add=True)

    name = models.CharField(max_length=100, )
    url = models.URLField(max_length=500)
    hash_type = models.CharField(max_length=10, choices=HASH_CHOICES)

    def __unicode__(self):
        return "<Project(%s)>" % self.name

    def is_today(self):
        return self.date_created.date() == datetime.date.today()
"""


import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

HASH_CHOICES = (
    (0, "MD5"),
    (1, "SHA1"),
    (2, "SHA256"),
    (3, "Git Tag"),
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # Other fields here
    accepted_eula = models.BooleanField()

    @staticmethod
    def create_by_signal(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    def __unicode__(self):
        return "<UserProfile(%s)>" % self.user

# Signal handler to automatically create a user profile when a user is created
post_save.connect(UserProfile.create_by_signal, sender=User)


class Project(models.Model):
    date_created = models.DateTimeField('date created')
    user = models.OneToOneField(User)

    name = models.CharField(max_length=100, )
    url = models.URLField(max_length=500)
    hash_type = models.CharField(max_length=10, choices=HASH_CHOICES)

    def __unicode__(self):
        return "<Project(%s)>" % self.name

    def is_today(self):
        return self.date_created.date() == datetime.date.today()

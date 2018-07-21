import datetime

from django.db import models
from django.utils import timezone


class Member(models.Model):
    github_username = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = self.github_username
        super(Member, self).save(*args, **kwargs)

    def get_latest_contribs(self):
        return list(map(
            lambda x: x.level,
            self.contrib_set.filter(date__gte=datetime.date.today()-datetime.timedelta(7))
        ))

    def __str__(self):
        return str(self.github_username)


class Contrib(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    level = models.PositiveIntegerField()

    def __str__(self):
        return str(self.member.github_username) + " / " + str(self.date) \
               + " / " + str(self.level)

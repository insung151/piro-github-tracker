from django.db import models


class Member(models.Model):
    git_user_name = models.CharField(max_length=100,)

    def __str__(self):
        return str(self.git_user_name)


class Contrib(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    level = models.PositiveIntegerField()

    def __str__(self):
        return str(self.member.git_user_name) + " / " + str(self.date) \
               + " / " +str(self.level)

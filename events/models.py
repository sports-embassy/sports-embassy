from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    spots = models.IntegerField()
    outside = models.BooleanField()
    date = models.DateTimeField()
    frequence = models.CharField(max_length=20)
    group = models.ForeignKey(SportGroup)
    sport_type = models.ForeignKey(SportType)
    target = models.ForeignKey(TargetGroup)


class SportGroup(models.Model):
    pass


class SportType(models.Model):
    pass


class TargetGroup(models.Model):
    pass


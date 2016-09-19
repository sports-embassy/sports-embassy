from django.db import models


class SportType(models.Model):
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sporttyp"
        verbose_name_plural = "Sporttypen"
        ordering = ['title']


class SportGroup(models.Model):
    title = models.CharField(max_length=50, blank=False)
    sport_type = models.ForeignKey(SportType)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sportart"
        verbose_name_plural = "Sportarten"
        ordering = ['title']


class TargetGroup(models.Model):
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Zielgruppe"
        verbose_name_plural = "Zielgruppen"
        ordering = ['title']


class EventDate(models.Model):
    date = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "Eventtermin"
        verbose_name_plural = "Eventtermine"
        ordering = ['date']


class Event(models.Model):

    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.TextField(blank=False)
    spots = models.IntegerField(blank=False)
    outside = models.BooleanField(blank=False)
    group = models.ForeignKey(SportGroup, blank=False)
    target = models.ForeignKey(TargetGroup, blank=False)
    dates = models.ManyToManyField(EventDate, through='EventOnEventDate', blank=False)

    def __str__(self):
        return self.title


class EventOnEventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCADE)
    takes_place = models.BooleanField(blank=False)

    def __str__(self):
        return self.event.title + ' am ' + str(self.event_date.date)

    class Meta:
        verbose_name = "Event am Termin"
        verbose_name_plural = "Events am Termin"

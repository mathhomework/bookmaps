from django.db import models

# Create your models here.


class Time(models.Model):
    time = models.PositiveSmallIntegerField()

    def natural_key(self):
        return {
            "id": self.id,
            "time": self.time
        }

    def __unicode__(self):
        return u"{}".format(self.time)


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def natural_key(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def __unicode__(self):
        return u"{}".format(self.name)


class Author(models.Model):
    name = models.CharField(max_length=150)

    def natural_key(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def __unicode__(self):
        return u"{}".format(self.name)


class Place(models.Model):
    name = models.CharField(max_length=150)
    lat = models.FloatField(blank=True, null=True, unique=True)
    lng = models.FloatField(blank=True, null=True, unique=True)

    def natural_key(self):
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.lat,
            "lng": self.lng
        }

    def __unicode__(self):
        return u"{}".format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True)
    time = models.ManyToManyField(Time, related_name="books", blank=True, null=True)
    subject = models.ManyToManyField(Subject, related_name="books", blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u"{}".format(self.title)



from django.contrib.gis.db import models


class Subject(models.Model):
    pass


class Collection(Subject):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('Collection', null=True, blank=True)

    def __unicode__(self):
        if self.parent:
            return self.parent.name + " | " + self.name
        else:
            return self.name


class Item(Subject):
    name = models.CharField(max_length=30)
    collection = models.ForeignKey(Collection)

    def __unicode__(self):
        return self.name + " in " + self.collection.name

    class Meta:
        unique_together = (('name', 'collection'),)


class Situation(Subject):
    item = models.ForeignKey(Item)
    begin = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

from django.db import models


class Subject(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    isA = models.CharField(max_length=30)
    namespace = models.URLField()


class Predicate(models.Model):
    name = models.CharField(max_length=30)
    namespace = models.URLField()

    class Meta:
        abstract = True


class Relationship(Predicate):
    subject = models.ForeignKey(Subject, related_name='related_to')
    obj = models.ForeignKey(Subject, related_name='related_from')


class Reference(Predicate):
    subject = models.ForeignKey(Subject, related_name='reference')
    url = models.URLField()


class Literal(Predicate):
    subject = models.ForeignKey(Subject, related_name='literal')


class TextLiteral(Literal):
    value = models.TextField()


class Collection(Subject):
    name = models.CharField(max_length=30, null=True, blank=True)
    parent = models.ForeignKey('Collection')


class Item(Subject):
    name = models.CharField(max_length=30, null=True, blank=True)
    collection = models.ForeignKey(Collection)


class Situation(Subject):
    begin = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    item = models.ForeignKey(Item)

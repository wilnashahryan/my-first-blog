from django.db import models

class Day(models.Model):
    day = models.CharField(max_length=10)

    def __unicode__(self):
        return self.day

class Network(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Show(models.Model):
    day = models.ForeignKey(Day)
    title = models.CharField(max_length=200)
    network = models.ForeignKey(Network)
    description = models.TextField()
    comment = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title

from __future__ import unicode_literals
from django.db import models
import os


class Advisor(models.Model):
    titleChoices = (
        ('P', 'Professor'),
        ('AP', 'Associate Professor'),
        ('I', 'Instructor'),
        ('NA', 'Not Available'))
    name = models.CharField(max_length=20)
    title = models.CharField(choices=titleChoices, max_length=100)
    age = models.SmallIntegerField()
    research = models.CharField(max_length=200)
    introduction = models.TextField()
    photo = models.ImageField(upload_to=os.path.dirname(os.path.realpath(__file__))+'/static/faces/')

    def __str__(self):
        return self.name


class Student(models.Model):
    uid = models.SmallIntegerField()
    name = models.CharField(max_length=20)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name + ': ' + str(self.uid) + ' advised by ' + self.advisor.name

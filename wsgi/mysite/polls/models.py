from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

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
    photo = models.ImageField(upload_to='/faces')

    def __str__(self):
        return self.name


class Selection(models.Model):
    student = models.ForeignKey(User, unique=True)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "student " + str(self.student) + " is advised by " + self.advisor.name

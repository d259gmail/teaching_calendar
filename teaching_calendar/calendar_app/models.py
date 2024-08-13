from django.db import models

from teaching_calendar.users.models import User


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=50)
    teachers = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'calendar_app'


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'calendar_app'

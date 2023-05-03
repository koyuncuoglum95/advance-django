from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    # After sending form, it will redirect you here
    def get_absolute_url(self):
        return reverse("advcbv:detail", kwargs={"pk": self.pk})
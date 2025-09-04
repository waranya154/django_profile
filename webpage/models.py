
from django.db import models

PREFIX_CHOICES = [
  ('นาย', 'นาย'),
  ('นาง', 'นาง'),
  ('นางสาว', 'นางสาว'),
]


class Student(models.Model):
  stid = models.CharField(max_length=10, unique=True)
  name_prefix = models.CharField(choices=PREFIX_CHOICES, max_length=10)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField(default=18)

  def __str__(self):
    return str(self.stid)


class Subjects(models.Model):
  sjid = models.CharField(max_length=10, unique=True)
  subjects_name = models.CharField(max_length=50)
  teacher_name = models.CharField(max_length=50)

  def __str__(self):
    return str(self.sjid)
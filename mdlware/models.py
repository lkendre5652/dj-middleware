from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Student1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


    def __str__(self):
        return self.name
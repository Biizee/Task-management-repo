from django.db import models

# Create your models here.
    
class User(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=400)
    status = models.CharField(max_length=25)
    task_owner = models.ManyToManyField("User", related_name="owner")

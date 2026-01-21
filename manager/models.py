from django.db import models

# Create your models here.
    
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=25)
    task_owner = models.ManyToManyField("User", related_name="owner")

    def __str__(self):
        return self.name

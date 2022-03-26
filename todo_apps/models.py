from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200)
    assigned_users = models.ManyToManyField(User)

    def __str__(self):
        return self.project_title

class Task(models.Model):
    text_title = models.CharField(max_length=200)
    text_desc = models.TextField(max_length=10000, blank=True, null=True,)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=10000, blank=True, null=True)
    date_due = models.DateField()
    status = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.text_title



    
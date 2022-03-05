from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    text_title = models.CharField(max_length=200)
    text_desc = models.TextField(max_length=10000, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.text_title
    
from dataclasses import fields
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text_title', 'text_desc', 'comment']
        labels = {'text_title': 'Title', 'text_desc': 'Description', 'comment': 'Comment',}
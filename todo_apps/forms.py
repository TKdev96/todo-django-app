from dataclasses import fields
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text_title', 'text_desc']
        labels = {'text_title': '', 'text_desc': ''}
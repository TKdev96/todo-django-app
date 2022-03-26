from django import forms
from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'assigned_users']
        labels = {'project_title': 'Name', 'assigned_users': 'Assigned users'}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text_title', 'text_desc', 'comment', 'date_due', 'owner', 'status', 'project']
        labels = {'text_title': 'Title', 'text_desc': 'Description', 'comment': 'Comment', 'date_due': 'Due date', 'owner': 'Owner', 'status': 'Status', 'project': 'Project'}


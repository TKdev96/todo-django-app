from django.contrib import admin

from todo_apps.models import Task, Project

# Register your models here.

admin.site.register(Task)
admin.site.register(Project)




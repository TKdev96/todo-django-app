from imp import reload
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import Http404, HttpResponse
import json

def check_topic_owner(request, task):
    if task.owner != request.user:
        raise Http404



# Delete a task.
@login_required
def delete_task(request, task_id):
    task_to_delete = Task.objects.get(id=task_id)
    task_to_delete.delete()

    return redirect('todo_apps:tasks')    

# Create your views here.

def index(request):
    return render(request, 'todo_apps/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')

    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_apps:tasks')    

    context = {'tasks': tasks}
    return render(request, 'todo_apps/tasks.html', context)

@login_required
def new_task(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            newtask = form.save(commit=False)
            newtask.owner = request.user
            newtask.save()
            return redirect('todo_apps:tasks')    

    context = {'form': form}
    return render(request, 'todo_apps/new_task.html', context)

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()


    context = {'task': task, "form": form}
    return render(request, 'todo_apps/edit_task.html', context)


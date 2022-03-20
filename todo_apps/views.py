from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import Http404


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

@login_required
def index(request):
    tasks = Task.objects.filter(owner=request.user, status=False) #for badge counter on index.html
    all_tasks = Task.objects.filter(status=False)
    context = {'tasks': tasks, 'all_tasks': all_tasks}
    return render(request, 'todo_apps/index.html', context)

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user, status=False).order_by('date_due')
    all_tasks = Task.objects.filter(status=False)

    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_apps:tasks')    

    context = {'tasks': tasks, 'all_tasks': all_tasks}
    return render(request, 'todo_apps/tasks.html', context)

@login_required
def all_tasks(request):
    all_tasks = Task.objects.filter(status=False).order_by('date_due')
    tasks = Task.objects.filter(owner=request.user, status=False)
    context = {'all_tasks': all_tasks, 'tasks': tasks}
    return render(request, 'todo_apps/all_tasks.html', context)

@login_required
def completed_tasks(request):
    completed_tasks = Task.objects.filter(status=True).order_by('date_due')
    all_tasks = Task.objects.filter(status=False)
    tasks = Task.objects.filter(owner=request.user, status=False)
    context = {'completed_tasks': completed_tasks, 'all_tasks': all_tasks, 'tasks': tasks}
    return render(request, 'todo_apps/completed_tasks.html', context)

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


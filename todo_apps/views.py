from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task, User
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

    #return redirect('todo_apps:tasks')    

# Create your views here.

@login_required
def index(request):
    projects = Project.objects.filter(assigned_users=request.user)
    tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), owner=request.user, status=False) #for badge counter on index.html
    all_tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), status=False)
    context = {'projects': projects,'tasks': tasks, 'all_tasks': all_tasks}
    return render(request, 'todo_apps/index.html', context)

@login_required
def tasks(request):
    tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), owner=request.user, status=False).order_by('date_due') #display tasks that are assigned to the same project as the user
    all_tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), status=False)

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
    all_tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), status=False).order_by('date_due')
    tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user),owner=request.user, status=False)
    context = {'all_tasks': all_tasks, 'tasks': tasks}
    return render(request, 'todo_apps/all_tasks.html', context)

@login_required
def completed_tasks(request):
    completed_tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), status=True).order_by('date_due')
    all_tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), status=False)
    tasks = Task.objects.filter(project = Project.objects.get(assigned_users=request.user), owner=request.user, status=False)
    context = {'completed_tasks': completed_tasks, 'all_tasks': all_tasks, 'tasks': tasks}
    return render(request, 'todo_apps/completed_tasks.html', context)

@login_required
def new_task(request):
    if request.method != 'POST':
        assigned = Project.objects.get(assigned_users=request.user)
        print(assigned)
        form = TaskForm(initial={'owner': request.user, 'project': assigned})
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            newtask = form.save(commit=False)
            #newtask.owner = request.user
            newtask.project = Project.objects.get(assigned_users=request.user)
            newtask.save()
            # return redirect('todo_apps:tasks') naprawia - usuniecie ładowania w zadań w modalu

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
            edit_task = form.save(commit=False)
            edit_task.project = Project.objects.get(assigned_users=request.user)
            edit_task.save()
            # return redirect('todo_apps:tasks') usunięcie naprawia bląd ładowania widoku wewnątrz modala


    context = {'task': task, "form": form}
    return render(request, 'todo_apps/edit_task.html', context)



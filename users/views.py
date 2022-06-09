from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserForm, UserCreationForm
from todo_apps.models import Project, User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



# Create your views here.
@login_required
def logout_view(request): 
    logout(request)
    return redirect('todo_apps:index')

def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST) #przekazanie danych formularza do klasy formularza tworzenia użytkownika

        if form.is_valid():
            new_user = form.save() #zapisanie w bazie nazwy użytkownika i hasła(hash)
            project = Project.objects.get(project_title='project_none') #odfiltrowanie i przypisanie defaultowego projektu do zmiennej 
            project.assigned_users.add(new_user) #dodanie nowego użytkownika do defaultowego projektu
            login(request, new_user) #autologowanie utworzonego użytkownika
            return redirect('todo_apps:index') #przekierowanie użytkownika na stronę główną

    context = {'form': form}
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
           #return redirect('users:profile')
    else:
            user_form = UpdateUserForm(instance=request.user)

    context = {'user_form': user_form}
    return render(request, 'users/profile.html', context)

@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Your password was successfully updated!', extra_tags='alert-success')
            #return redirect('edit_password')
        else:
            messages.error(request, 'Error, please enter passwords again.', extra_tags='alert-danger')    
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/edit_password.html', {
        'form': form
    })


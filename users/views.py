from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateUserForm, UserCreationForm
from todo_apps.models import Project, User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = 'Successfully Change Your Password'
    succes_url = reverse_lazy('index')


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
            return redirect('users:profile')
    else:
            user_form = UpdateUserForm(instance=request.user)

    context = {'user_form': user_form}
    return render(request, 'users/profile.html', context)


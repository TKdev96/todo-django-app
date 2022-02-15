from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request): 
    logout(request)
    return redirect('todo_apps:index')

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST) #przekazanie danych formularza do klasy formularza tworzenia użytkownika

        if form.is_valid():
            new_user = form.save() #zapisanie w bazie nazwy użytkownika i hasła(hash)
            login(request, new_user) #autologowanie utworzonego użytkownika
            return redirect('todo_apps:index') #przekierowanie użytkownika na stronę główną

    context = {'form': form}
    return render(request, 'users/register.html', context) 
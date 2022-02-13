from django.urls import path #import path

from . import views #import views

app_name = 'todo_apps'

urlpatterns = [
    #Dodanie strony głównej
    path('', views.index, name='index'),
] 
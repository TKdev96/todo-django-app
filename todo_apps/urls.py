from django.urls import path #import path

from . import views #import views

app_name = 'todo_apps'

urlpatterns = [
    #Dodanie strony głównej
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('new_task/', views.new_task, name="new_task"),
    path('edit_task/<int:task_id>/', views.edit_task, name="edit_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    ] 
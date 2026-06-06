from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.user_profile, name='profile'),
    path('addTask/', views.addTask, name='add_task'),
    path('tasks/pending/', views.pending_tasks, name='pending'),
    path('tasks/completed/', views.completed_tasks, name='completed'),
    path('deleteTask/', views.delete_task, name='delete_task'),
    path('completeTask/', views.complete_task, name='complete_task'),
    path('editTask/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail')
]
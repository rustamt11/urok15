from django.urls import path
from . import views

app_name = 'task_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'),
]

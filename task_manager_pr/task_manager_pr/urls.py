from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_tasks(request):
    return redirect('tasks:index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task_manager.urls', namespace='tasks')),
    path('', redirect_to_tasks, name='redirect_to_tasks'),
]

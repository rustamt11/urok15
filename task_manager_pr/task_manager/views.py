from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.filter(status='not_done').order_by('-deadline_date', '-priority')
    completed_tasks = Task.objects.filter(status='done').order_by('-priority')
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'task_manager/index.html', context)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:index')
    else:
        form = TaskForm()
    return render(request, 'task_manager/create_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager:index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_manager:index')

def mark_done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = 'done'
    task.save()
    return redirect('task_manager:index')

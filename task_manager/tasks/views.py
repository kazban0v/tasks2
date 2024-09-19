from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    
    category = request.GET.get('category')
    priority = request.GET.get('priority')
    
    if category:
        tasks = tasks.filter(category=category)
    if priority:
        tasks = tasks.filter(priority=priority)
    
    completed_tasks = tasks.filter(status='COMPLETED').count()
    total_tasks = tasks.count()
    completion_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'completion_percentage': completion_percentage,
    })

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
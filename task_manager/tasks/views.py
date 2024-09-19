from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

def task_completion_percentage(user):
    total_tasks = Task.objects.filter(user=user).count()
    completed_tasks = Task.objects.filter(user=user, status='Completed').count()
    if total_tasks == 0:
        return 0
    return (completed_tasks / total_tasks) * 100

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')  # Перенаправление на страницу входа после регистрации
    template_name = 'registration/signup.html'  # Шаблон для регистрации

def home(request):
    if request.user.is_authenticated:
        return redirect('task_list')  # Перенаправление на список задач, если пользователь уже вошёл
    return render(request, 'tasks/home.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

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
    task.delete()
    return redirect('task_list')

def custom_logout(request):
    logout(request)  # Выход из системы
    return redirect('home')  # Перенаправление на начальную страницу

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST

from .models import Task


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    tasks = Task.objects.filter(
        user=request.user,
        is_completed=False
    ).order_by('-updated_at')

    completed_tasks = Task.objects.filter(
        user=request.user,
        is_completed=True
    ).order_by('-updated_at')

    return render(request, 'home.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'total_tasks': tasks.count() + completed_tasks.count(),
        'pending_count': tasks.count(),
        'completed_count': completed_tasks.count(),
    })


@login_required
@require_POST
def addTask(request):
    task_text = request.POST.get('task', '').strip()

    if task_text:
        Task.objects.create(
            task=task_text,
            user=request.user
        )

    return redirect('home')


@login_required
@require_POST
def completeTask(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.is_completed = True
    task.save()

    return redirect('home')


@login_required
@require_POST
def deleteTask(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()
    return redirect('home')


@login_required
def editTask(request, task_id):
    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    if request.method == 'POST':
        new_task = request.POST.get('task', '').strip()

        if new_task:
            task.task = new_task
            task.save()
            return redirect('home')

        return render(
            request,
            'edit.html',
            {'task': task, 'error': 'Task cannot be empty.'}
        )

    return render(request, 'edit.html', {'task': task})

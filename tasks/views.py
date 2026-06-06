from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks': tasks,
        'tasks_count': tasks.count()
    }
    return render(request, "tasks/home.html", context)

@login_required
def user_profile(request):
    user = request.user
    
    # Обработка POST-запроса (сохранение email)
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        user.email = email
        user.save()
        messages.success(request, 'Email успешно обновлён!')
        return redirect('profile')
    
    total_tasks = Task.objects.filter(user=user).count()
    completed_tasks = Task.objects.filter(user=user, completed=True).count()
    pending_tasks = Task.objects.filter(user=user, completed=False).count()
    
    if total_tasks > 0:
        completion_rate = round((completed_tasks / total_tasks) * 100)
    else:
        completion_rate = 0
    
    context = {
        'user': user,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'completion_rate': completion_rate,
    }
    return render(request, 'tasks/profile.html', context)

@login_required
def addTask(request):
    if request.method == 'POST':
        task_name = request.POST.get('name', '').strip()
        desc = request.POST.get('description', '').strip()
        
        if not task_name:
            messages.error(request, 'Название задачи не может быть пустым!')
        else:
            Task.objects.create(
                title=task_name,
                description=desc,
                user=request.user
            )
            messages.success(request, f'Задача "{task_name}" добавлена!')
    
    return HttpResponseRedirect('/')

@login_required
def pending_tasks(request):
    tasks = Task.objects.filter(completed=False, user=request.user)
    context = {
        'tasks': tasks,
        'tasks_count': tasks.count(),
        'title': 'Невыполненные задачи',
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(completed=True, user=request.user)
    context = {
        'tasks': tasks,
        'tasks_count': tasks.count(),
        'title': 'Выполненные задачи',
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def complete_task(request):
    task_id = request.POST.get('task_id')
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect('/')

@login_required
def delete_task(request):
    task_id = request.POST.get('task_id')
    if task_id:
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.delete()
    return HttpResponseRedirect('/')

@login_required
def edit_task(request):
    task_id = request.POST.get('task_id')
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    task_name = request.POST.get('name')
    desc = request.POST.get('description')
    
    if task_name:
        task.title = task_name
    task.description = desc
    task.save()
    return HttpResponseRedirect('/')

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)
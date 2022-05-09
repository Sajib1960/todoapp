from multiprocessing import context
from django.shortcuts import redirect, render

from .models import *
from .forms import *
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    task_items = Task.objects.order_by("id")
    form = TaskForm()
    context = {'task_items' : task_items, 'form' : form}
    return render(request, "mylist/index.html", context)

@require_POST
def addTask(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        new_task = Task(text=request.POST['text'])
        new_task.save()

    return redirect('index')


def completedTask(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()

    return redirect('index')


def delete_completedTask(request):
    Task.objects.filter(completed__exact =True).delete()

    return redirect('index')


def delete_allTask(request):
    Task.objects.all().delete()

    return redirect('index')
from multiprocessing import context
from django.shortcuts import render

from .models import *

# Create your views here.

def index(request):
    task_items = Task.objects.order_by("id")
    context = {'task_items' : task_items}
    return render(request, "mylist/index.html", context)
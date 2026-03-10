from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'core/task_list.html', {'tasks': tasks})

def about_view(request):
    # You can fetch data from Supabase here if needed
    context = {
        "description": "This is a dynamic description from the view!"
    }
    return render(request, 'core/about.html', context)

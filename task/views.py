from django.contrib import messages
from django.shortcuts import render
from accounts.models import User
from office.models import Office
from task.models import Task
from django.db.models import ObjectDoesNotExist

office = Office.objects.all()
task_force = User.objects.all()




def task(request):
    try:
        user = User.objects.get(username=request.user, organizations__contains="Employee")
    except ObjectDoesNotExist:
        user = None
    context = {
        'user': user,
        'office': office,
        'task_force': task_force,
    }
    if request.method == 'POST':
        __office = request.POST['office']
        task__force = request.POST['task_force']
        task_object = request.POST['task_object']
        task_description = request.POST['task_description']
        datefield = request.POST['dateField']
        try:
            user_do_task = User.objects.get(organizations=__office, username=task__force)
        except ObjectDoesNotExist:
            return render(request, 'task.html', context, messages.ERROR(request, "You cant do that"))
        task = Task(task_title=task_object, task_description=task_description,
                    dead_line=datefield, task_force=user_do_task)
        task.save()
        return render(request, 'dashboard.html', messages.success(request, "Your task is up now"))
    else:
        return render(request, 'task.html', context)
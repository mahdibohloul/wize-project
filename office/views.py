from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import UserManager, User
from .admin import OfficeAdmin
from .models import Office
from task.models import Task
from django.db.models import ObjectDoesNotExist


def apply(request):
    if request.method == 'POST':
        # office = request.POST['office']
        # user = User.objects.get_by_natural_key(email=request.user)
        # # user = request.user
        # # user = User(email=user.email, password=user.password, is_staff=user.is_staff,
        # #                                 is_superuser=user.is_superuser, job_class='OE', office=office)
        # user.office = office
        # user.job_class = 'OE'
        # user.save()
        # return redirect('dashboard')
        raw = request.POST['accept_apply']
        message = raw.split(" of ", 1)
        simple = message[1].split(" to ")
        if message[0] == 'request_for_work':
            user = User.objects.get(username=simple[0])
            user.job_class = "Office Employee"
            user.organizations = simple[1]
            user.save()
        return render(request, 'dashboard.html')
    else:
        return render(request, 'dashboard.html')


def dashboard(request):

    try:
        user = User.objects.get(job_class__exact='Employee', username=request.user)

        context ={
            'nameofuser': user,
            'username': request.user,

        }
        return render(request, 'dashboard.html', context)
    except ObjectDoesNotExist:
        try:
            task_force = User.objects.get(job_class='Office Employee', username=request.user)
            task_date = Task.objects.order_by('dead_line').filter(task_force=task_force)
            context = {
                'task_force': task_force,
                'username': request.user,
                'task_date': task_date,

            }
            return render(request, 'dashboard.html', context)
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(is_staff=True, username=request.user)
                messages = [user.notification.message]
                officeaplly = [user.notification.office.office]
                userapplicant = [user.notification.recipient.username]
                my_list = zip(messages,userapplicant,officeaplly)
                context = {
                    'staff_user': None,
                    'username': request.user,
                    'my_list': my_list,
                }
                return render(request, 'dashboard.html', context)
            except ObjectDoesNotExist:
                context = {
                    # 'user': None,
                    'username': request.user,
                }
            return render(request, 'dashboard.html', context)


def is_done(request):
    if request.method == 'POST':
        is_done = request.POST['is_done']
        task_force = request.user
        task = Task.objects.get(task_force=task_force)
        task.is_done = bool(is_done)
        task.save()
        return render(request, 'dashboard.html', messages.success(request, "Your task is done!"))
    else:
        return render(request, 'dashboard.html')


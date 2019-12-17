from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Messages
from accounts.models import User
from django.db.models import ObjectDoesNotExist
from .choices import object_messages
from office.models import Office
from django.db.models import F


# def apply(request):
#     # try:
#
#     return render(request, 'apply.html', context)
#     # except ObjectDoesNotExist:
#     #     office = Office.office
#     #     user_manager = User.objects.get(job_class='Office Employee', username=request.user)
#     #     context = {
#     #         'user': request.user,
#     #         'object_messages': object_messages,
#     #         'office': office,
#     #         'user_manager': user_manager
#     #     }
#     #     return render(request, 'apply.html', context)
#     #


office = Office.objects.all()
context = {
    'object_messages': object_messages,
    'office': office,
}


def notification(request):
    if request.method == 'POST':
        recipient = request.user
        office = request.POST['office']
        message = request.POST['object_messages']
        if message == "request_for_work":
            try:
                applicant = User.objects.get(job_class="Employee", username=request.user)
                try:
                    manager_office = User.objects.get(job_class='Office Manager')
                except ObjectDoesNotExist:
                    manager_office = User.objects.get(is_superuser=True, is_staff=True)
                notify = Messages(message=message, recipient=applicant, office=Office.objects.get(office=office))
                notify.save()
                for i in [manager_office]:
                    manager_office.notification = notify
                    manager_office.save()

                return render(request,'dashboard.html', messages.success(request, 'Your apply is submitted'),context)

            except ObjectDoesNotExist:

                return render(request, 'apply.html', messages.error(request, 'You cant apply for this job'),context)
        else:
            applicant = User.objects.get(job_class="Employee", username=request.user)
            admin = User.objects.get(is_staff=True, is_superuser=True)
            notify = Messages(message=message, recipient=applicant, office=Office.objects.get(office=office))
            notify.save()
            for i in [admin]:

                admin.notification = notify
                admin.save()
            return render(request, 'dashboard.html', messages.success(request, "Your apply is submitted"),context)
    else:
        return render(request, 'apply.html', context)




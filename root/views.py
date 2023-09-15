from django.shortcuts import render
from .models import *
from course.models import Courses,Trainer


def home(request):
    services = Services.objects.filter(status=True)[:3]
    last_three_course = Courses.objects.filter(status=True)[:3]
    last_three_trainer = Trainer.objects.filter(status=True)[:3]
    context = {'service':services,
               'course':last_three_course,
               'trainer':last_three_trainer,
               
               }
    return render(request,"root/index.html",context=context)
# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def about(request):
    return render(request,"root/about.html")
# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def contact(request):
    return render(request,"root/contact.html")
# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def trainer(request):
    return render(request,"root/trainers.html")
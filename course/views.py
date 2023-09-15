from django.shortcuts import render
from .models import *

def Maincourse(request,cat=None,teacher=None):
    if cat:
        courses = Courses.objects.filter(category__name=cat)
    elif teacher:
        courses = Courses.objects.filter(teacher__info__username = teacher)
    else:
        courses = Courses.objects.filter(status = True)
    context = {
        'maincourse': courses
    }
    return render(request,"courses/courses.html",context=context)
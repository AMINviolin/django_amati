from django.shortcuts import render
from .models import *

def Maincourse(request):
    courses = Courses.objects.filter(status=True)
    context = {
        'maincourse': courses
    }
    return render(request,"courses/courses.html",context=context)
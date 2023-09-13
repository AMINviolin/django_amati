from django.shortcuts import render
from .models import *

def Maincourse(request):
    courses = Courses.objects.filter(status=True)
    context = {
        'maincourse': courses
    }
    return render(request,"course/courses.html",context=context)
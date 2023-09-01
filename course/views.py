from django.shortcuts import render
from .models import *

def course(request):
    courses = Courses.objects.filter(status=True)
    context = {
        'courses': courses
    }
    return render(request,"course/courses.html",context=context)
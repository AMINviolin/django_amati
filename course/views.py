from django.shortcuts import render
from .models import *

def course(request):
    return render(request,"course/courses.html")
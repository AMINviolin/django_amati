from django.shortcuts import render
from .models import *


def home(request):
    services = Services.objects.filter(status=True)[:3]
    context = {'service':services}
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
from django.shortcuts import render
from .models import service


def home(request):
    return render(request,"root/index.html",context = {'name': 'admin'})

def about(request):
    return render(request,"root/about.html",context = {'make': '1998'})

def contact(request):
    return render(request,"root/contact.html",context = {'number': '45346'})
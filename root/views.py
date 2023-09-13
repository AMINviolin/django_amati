from django.shortcuts import render
from .models import *


def home(request):
    web = WebDevelopment.objects.all()
    market = Marketing.objects.all()
    cont = Content.objects.all()
    context = {'web': web, 'market': market, 'cont': cont}
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
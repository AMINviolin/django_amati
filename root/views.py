from django.shortcuts import render



def home(request):
    return render(render,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
from django.shortcuts import render,redirect
from .models import Services,NewsLetter
from course.models import Courses,Trainer
from course.models import Category
from accounts.models import CustomUser
from .forms import NewsLetterForm,ContactUsForm
from django.contrib import messages

def home(request):    
    if request.method == 'GET':
        return render(request,"root/index.html")
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'email submited')
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:home')
# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def about(request):
    if request.method == 'GET':
        trainer = Trainer.objects.filter(status = True)
        context = {
            'trainer':trainer,
        }
        return render(request,"root/about.html",context = context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'email submited')
            return redirect('root:about')
        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:about')
# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&


# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def contact(request):
    if request.method == 'GET':
        return render(request,"root/contact.html")
    elif request.method == 'POST' and len(request.POST) == 2:
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'email submited')
            return redirect('root:contact')
        else:
            messages.add_message(request,messages.ERROR,'invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) > 2:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your message sent and we will answer to it soon')
            return redirect('root:contact')
        else:
            messages.add_message(request,messages.ERROR,'invalid input data')
            return redirect('root:contact')

# _&_&_&_&_&_&_&_&_&_&_&_&_&_&_&_&

def trainer(request):
    return render(request,"root/trainers.html")
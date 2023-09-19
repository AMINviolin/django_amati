from django.shortcuts import render,redirect
from.forms import CustomUserCreation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'registration/login.html',context={'form':form})
    else:
        if '@' in request.POST.get('username'):
            username = User.objects.get(email=request.POST.get('username')).username
        form =AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect(request.path_info)

@login_required
def Logout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        form = CustomUserCreation()
        return render(request, 'registration/signup.html',context={'form':form})
    
    else:
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    
            else:
                messages.add_message(request,messages.ERROR,'invalid data')
                return redirect(request.path_info)

        else:
            messages.add_message(request,messages.ERROR,'invalid data')
            return redirect(request.path_info)


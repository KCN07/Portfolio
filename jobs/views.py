from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Job
def home(request):
    jobs=Job.objects

    return render(request,'jobs/home.html',{'jobs':jobs})

def education(request):
    return render(request,'jobs/education.html')

def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user  :
            login(request,user)
            return redirect("home")
        else:
            return redirect('login')
    else:
       return render(request,'jobs/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

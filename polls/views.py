from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import Advisor, Student

def loginpage(request):
    print('function called')
    form = LoginForm
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print('user authenticated')
        if user.is_active:
            login(request, user)
            return index(request)
        else:
            print('user not active')
            return render(request, 'polls/login.html', {'form': form})
    else:
        return render(request, 'polls/login.html', {'form': form})

def index(request):
    if request.method == 'POST':
        stuName = request.POST['user']
        advName = request.POST['select']
        student = Student.objects.get(uid=stuName)
        student.advisor = advName
        student.save()
    allAdvisors = Advisor.objects.all()
    return render(request, 'polls/index.html', {'allAdvisors': allAdvisors})

def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            index(request)
        else:
            loginpage(request)
    else:
        loginpage(request)

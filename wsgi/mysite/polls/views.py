from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        if not user:
            return HttpResponseRedirect('login')
        elif user.is_active:
            login(request, user)
            return HttpResponseRedirect('index')
        else:
            print('user not active')
            return HttpResponseRedirect('login')
    else:
        return render(request, 'polls/login.html', {'form': form})


@login_required(login_url='login')
def index(request):
    print request.POST
    stuName = request.user.username
    allAdvisors = Advisor.objects.all()
    return render(request, 'polls/index.html', {'allAdvisors': allAdvisors, 'stuName': stuName})


@login_required(login_url='login')
def select(request, advisor=None):
    print advisor, request.user.username
    return HttpResponseRedirect('index')


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('login')

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Advisor, Student
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

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
            return index(request, user)
        else:
            print('user not active')
            return render(request, 'polls/login.html', {'form': form})
    else:
        return render(request, 'polls/login.html', {'form': form})

@login_required(login_url='login')
def index(request, user):
    print request.POST
    print user
    stuName = user.username
    if request.method == 'POST':
        print('index intrigued from post')
        if 'select' in request.POST:
            advName = request.POST['select']
            student = Student.objects.get(uid=stuName)
            student.advisor = advName
            student.save()
    allAdvisors = Advisor.objects.all()
    return render(request, 'polls/index.html', {'allAdvisors': allAdvisors, 'stuName': stuName})

def logoutView(request):
    logout(request)
    return loginpage(request)


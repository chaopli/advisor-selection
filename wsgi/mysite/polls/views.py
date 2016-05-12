from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Advisor, Selection
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


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


@login_required(login_url='/polls/login')
def index(request):
    print request.POST
    stuName = request.user.username
    allAdvisors = Advisor.objects.all()
    availableAdvisors, fullAdvisors = [], []
    for advisor in allAdvisors:
        if Selection.objects.filter(advisor=advisor).count() >= 5:
            fullAdvisors.append(advisor)
        else:
            availableAdvisors.append(advisor)
    state = 'selected'
    try:
        Selection.objects.get(student=request.user)
    except ObjectDoesNotExist:
        state = ''
    return render(request, 'polls/index.html', {'availableAdvisors': availableAdvisors,
                                                'stuName': stuName, 'state': state,
                                                'fullAdvisors': fullAdvisors})


@login_required(login_url='/polls/login')
def select(request, advisor=None):
    print advisor, request.user.username
    advisor = Advisor.objects.get(name=advisor)
    try:
        selection = Selection.objects.get(student=request.user)
    except ObjectDoesNotExist:
        selection = Selection(student=request.user, advisor=advisor)
        selection.save()
    return HttpResponseRedirect('index')


@login_required(login_url='/polls/login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('login')


@login_required(login_url='/polls/login')
def reselect(request):
    user = request.user
    try:
        Selection.objects.get(student=request.user).delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('index')

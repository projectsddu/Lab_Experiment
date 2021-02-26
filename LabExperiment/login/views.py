from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def create_user(request):
    # user = User.objects.create_user('virat','keval@keval.com','gandevia')
    # user.save()
    user = User.objects.get(first_name="Virat")
    print(user.first_name)
    print(user.last_name)
    return HttpResponse("Success")


@csrf_exempt
def login(request):
    return render(request, 'login.html', context=None)


def login_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if(user is not None):
        auth.login(request,user)
        return HttpResponseRedirect('http://127.0.0.1:8000/login/loggedin')
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/login/invalidloggedin')
    

def loggedin(request):
    return render(request,'loggedin.html',{'full_name': request.user.username})


def invalidloggedin(request):
    return render(request,'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

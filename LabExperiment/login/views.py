from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
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
    return render(request,'base.html',context=None)

@csrf_exempt
def login_user(request):
    
    if request.method == 'GET':
        return HttpResponse("<h1 style='color: red'>404 PAGE NOT FOUND</h1>")
    # else:
        # username = 
    
    return HttpResponse(" ")
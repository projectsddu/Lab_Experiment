from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="login"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout/',views.logout,name="logout"),
    path('loggedin/',views.loggedin,name="loggedin"),
    path('invalidloggedin/',views.invalidloggedin,name="invalidlogin")
]

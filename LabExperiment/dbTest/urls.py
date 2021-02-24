from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addstudent/',views.addStudent,name="addstudent"),
    path('deletestudent/',views.deleteStudent,name="deletestudent")
]

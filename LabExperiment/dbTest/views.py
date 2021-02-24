from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def addStudent(request):
    stu = Student.objects.create(student_name="keval",student_dob="2002-05-16",student_rollno=37)
    stu.save()
    return HttpResponse("Object created successfully.")

def deleteStudent(request):
    student = Student.objects.get(student_name="keval")
    print(student.student_name)
    print(student.student_dob)
    print(student.student_rollno)
    student.delete()
    return HttpResponse("Success")

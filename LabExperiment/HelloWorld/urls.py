from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_template,name="view_template")
]

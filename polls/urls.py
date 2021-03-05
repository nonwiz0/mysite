'''
Created on Mar 4, 2021

@author: Student
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]

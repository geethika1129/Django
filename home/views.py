from django.shortcuts import render,HttpResponse
from django.contrib import admin
from django.urls import path
from home import views

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

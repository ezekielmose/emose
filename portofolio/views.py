from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return  HttpResponse("<h2>This is my home page</h1>")
def post(request):
    return  HttpResponse("<h2>This is my posts page</h1>")
def posts(request):
    return  HttpResponse("<h2>Post</h1>")
def user_profile(request):
    return  HttpResponse("<h2>My profile</h1>")

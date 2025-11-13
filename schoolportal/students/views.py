from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Welcome to the Student Portal</h1>")


def about(request):
    return HttpResponse("<h1>About the Student Portal</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us at support@gmail.com")

def profile(request):
    return HttpResponse("<h1>Student Profile Page</h1>")
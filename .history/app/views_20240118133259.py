from django.shortcuts import render
from django.http import HttpResponse
from models import User

# Create your views here.

# create a function


def home(request):

    return HttpResponse("<h1>Welcome to Django</h1>")

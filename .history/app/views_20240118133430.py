from django.shortcuts import render
from django.http import HttpResponse
from models import UserInfo

# Create your views here.

# create a function


def home(request):
    obj = UserInfo(title="Django", description="Learning")
    obj.save()
    return HttpResponse("<h1>Welcome to Django</h1>")

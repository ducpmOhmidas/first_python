from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserInfo

# Create your views here.

# create a function


def home(request):
    content = UserInfo.objects.all()
    return HttpResponse("<h1>Welcome to Django</h1>")

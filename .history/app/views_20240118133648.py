from django.shortcuts import render
from django.http import HttpResponse
from models import UserInfo

# Create your views here.

# create a function


def home(request):
    # Adding objects
    obj = UserInfo(title="Django", description="Learning")
    obj.save()
    # Retrieving objects
    UserInfo.objects.all()
    # Modifying existing objects
    obj2 = UserInfo.objects.get
    return HttpResponse("<h1>Welcome to Django</h1>")
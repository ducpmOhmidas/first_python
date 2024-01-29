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
    obj2 = UserInfo.objects.get(id=1)
    obj2.title = "Django2"
    obj2.save()
    # Deleting objects
    obj3 = UserInfo.objects.get(id=1)
    obj3.delete()
    return HttpResponse("<h1>Welcome to Django</h1>")

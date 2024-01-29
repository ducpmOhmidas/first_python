from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserInfo
from django.shortcuts import render
from django import forms

# Create your views here.

# create a function


def home(request):
    content = UserInfo(title="Django",
                       description="Learning", image="https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg")
    content = UserInfo.objects.all()
    context = {
        'content': content
    }
    return render(request, "index.html", context=context)

def createUser(request):
    context = {}

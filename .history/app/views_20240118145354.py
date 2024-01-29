from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserInfo
from django.shortcuts import render

# Create your views here.

# create a function


def home(request):
    content = UserInfo.objects.all()
    context = {
        'content': content
    }
    return HttpResponse(request, "index.html", context=)

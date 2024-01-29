from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserInfo
from django.shortcuts import render

# Create your views here.

# create a function


def home(request):
    obj = GeeksModel(title="GeeksforGeeks",
   description="GFG is a portal for computer science students")
    content = UserInfo.objects.all()
    context = {
        'content': content
    }
    return render(request, "index.html", context=context)

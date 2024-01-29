from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# create a function
def geeks_view(request):
     
    return HttpResponse("<h1>Welcome to GeeksforGeeks</h1>")

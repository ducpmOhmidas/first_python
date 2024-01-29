from django.shortcuts import render
from app.models import UserInfo
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import UserSerializer

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
    context['form'] = UserInfo
    return render(request, "")


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer(data=)
    def get():
        
    def put():
        queryset = User.objects.all()
        serializer_class = UserSerializer(data=)

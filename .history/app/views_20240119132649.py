from django.shortcuts import render
from app.models import UserInfo
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import UserSerializer
from rest_framework.response import Response

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

    def get(self):
        queryset = self.get_queryset()
        serialize = UserSerializer(queryset)
        return Response(serialize)

    def post(self, request):
        queryset = self.get_queryset()
        serialize = UserSerializer(queryset, data=request)
        serialize.save()
        return Response(serialize.data)

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


def get_object(self):
    queryset = self.get_queryset()
    filter - {}
    for field in self.lookup_field:
        filter[field] = self.kwargs[field]
    obj = self.get_object_or_404(queryset, filter)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self):
        queryset = self.get_queryset()
        serialize = UserSerializer(queryset)
        return Response(serialize)

    def post(self):
        queryset = UserInfo.objects.filter(user=self.request.user)
        serialize = UserSerializer(queryset)
        serialize.save(user=self.request.user)
        return Response(serialize.data)

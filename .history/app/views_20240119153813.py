from django.shortcuts import render
from app.models import UserInfo
from django.contrib.auth.models import User
from rest_framework import viewsets
from app.serializers import UserInfoSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

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

# class MultipleFieldLookupMixin:
#     def get_object(self):
#         queryset = self.get_queryset()
#         filter = {}
#         for field in self.lookup_field:
#             filter[field] = self.kwargs[field]
#         obj = get_object_or_404(queryset, filter)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = self.get_queryset()
        context = {'request': request}
        serializer = UserInfoSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.get(pk=pk)
        serializer = UserInfoSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = User.objects.get(pk=pk)
        serializer = UserInfoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        instance = User.objects.get(pk=pk)
        instance.delete()
        return Response(status=204)

class CustomAuthToken(ObtainAuthToken):
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

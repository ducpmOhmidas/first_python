from .models import UserInfo
from rest_framework import serializers

# Serializers define the API representation.


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'created_on', 'image']

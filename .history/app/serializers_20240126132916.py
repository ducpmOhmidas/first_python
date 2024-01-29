from .models import UserInfo
from rest_framework import serializers

# Serializers define the API representation.


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['title', 'description',
                  'description2', 'created_on', 'image']

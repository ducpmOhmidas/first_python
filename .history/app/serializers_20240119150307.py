from .m import User
from rest_framework import serializers

# Serializers define the API representation.


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

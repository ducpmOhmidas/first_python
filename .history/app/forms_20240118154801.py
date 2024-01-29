
from django import forms
from .models import UserInfo
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'image']
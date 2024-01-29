
from django import forms
from .models import User
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'image']
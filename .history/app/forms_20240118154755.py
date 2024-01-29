
from django import forms
from .m
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'image']
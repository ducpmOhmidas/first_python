
from django import forms
from .models import 
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'image']
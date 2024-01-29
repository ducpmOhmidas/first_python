
from django import forms
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserInfo
        fields = ['title', 'description', 'image']
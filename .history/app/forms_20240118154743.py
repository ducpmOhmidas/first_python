
from django import forms
 
class UserForm(forms.Form):
 
    class Meta:
        model = UserForm
        fields = ['title', 'description', 'image']
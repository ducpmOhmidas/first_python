
from django import forms
 
class UserForm(forms.Form):
 
    class Meta:
        model = Use
        fields = ['title', 'description', 'image']
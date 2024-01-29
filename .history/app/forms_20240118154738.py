
from django import forms
 
class UserForm(forms.Form):
 
    class Meta:
        model = GeeksModel
        fields = ['title', 'description', 'image']
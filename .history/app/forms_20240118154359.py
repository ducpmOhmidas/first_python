
from django import forms
 
class GeeksForm(forms.Form):
 
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
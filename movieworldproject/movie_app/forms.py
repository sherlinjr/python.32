from django import forms
from .models import Movieworld

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movieworld
        fields=['name','desc','year','img']
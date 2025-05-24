from django import forms
from .models import loginForm

class partialloginform(forms.ModelForm):
    class Meta:
        model = loginForm()
        fields = '__all__'
    
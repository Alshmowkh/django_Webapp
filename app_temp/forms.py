from django import forms
from .models import Student
class Formy(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
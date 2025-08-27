from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'gender', 'agree']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bob Smith'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'agree': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
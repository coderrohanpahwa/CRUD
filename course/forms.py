from django import forms
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter name','email':'Enter email','password':'Enter password'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
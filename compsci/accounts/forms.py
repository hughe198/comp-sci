from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import NewUser

class RegistationForm(UserCreationForm):
    email = forms.EmailField(max_length =255, help_text ="Required: Valid Email")

    class Meta:
        model = NewUser
        fields= ('email','user_name','first_name','password1','password2')


class login_form(forms.ModelForm):

    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ("email", "password")

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email = email,password = password):
            raise forms.ValidationError("Invalid Login")

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    # help_text : 해당 field를 작성하는 곳 옆에 나타남.

    class Meta:
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")


class ProfileAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            # self : form
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                print("non")
                raise forms.ValidationError("Invaild login")

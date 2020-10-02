from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    # help_text : 해당 field를 작성하는 곳 옆에 나타남.

    class Meta:
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")

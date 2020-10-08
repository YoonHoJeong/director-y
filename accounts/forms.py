from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db import transaction

from .models import Profile, Actor, Director, Staff


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    # help_text : 해당 field를 작성하는 곳 옆에 나타남.

    class Meta:
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")


class DirectorRegistraionForm(UserCreationForm):
    awards = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")

    @transaction.atomic  # 모든 함수가 한번에 처리됨.
    def save(self):
        profile = super().save(commit=False)
        # commit=False 바로 저장하지 않고 u_type을 설정하고 저장

        profile.u_type = 1
        profile.save()
        director = Director.objects.create(profile=profile)
        director.awards = self.cleaned_data.get('awards')
        director.save()
        return profile


class ActorRegistraionForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    company = forms.CharField(max_length=30, required=True)
    height = forms.IntegerField(required=True)
    weight = forms.IntegerField(required=True)
    specialty = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")

    @transaction.atomic  # 모든 함수가 한번에 처리됨.
    def save(self):
        profile = super().save(commit=False)

        profile.u_type = 2
        profile.save()
        actor = Actor.objects.create(profile=profile)
        actor.company = self.cleaned_data.get('company')
        actor.height = self.cleaned_data.get('height')
        actor.weight = self.cleaned_data.get('weight')
        actor.specialty = self.cleaned_data.get('specialty')
        actor.save()
        return profile


class StaffRegistraionForm(UserCreationForm):
    role = forms.CharField(max_length=30)
    tool_list = forms.CharField(max_length=200)

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ("email", "username", "password1",  "password2", "name",
                  "name_eng", "age", "date_of_birth", "avatar", "intro", "education")

    @transaction.atomic  # 모든 함수가 한번에 처리됨.
    def save(self):
        profile = super().save(commit=False)

        profile.u_type = 3
        profile.save()
        staff = Staff.objects.create(profile=profile)
        staff.role = self.cleaned_data.get('role')
        staff.tool_list = self.cleaned_data.get('tool_list')
        staff.save()
        return profile


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
                raise forms.ValidationError("Invaild login")

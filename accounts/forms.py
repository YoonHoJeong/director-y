from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db import transaction

from .models import Profile, Actor, Director, Staff, SNS
from main.models import ActorImage


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=60, help_text='Required. Add a valid email address')
    # help_text : 해당 field를 작성하는 곳 옆에 나타남.


    class Meta:
        FIELDS = ("email", "username", "password1", "password2", "name", "date_of_birth")
        model = Profile
        fields = FIELDS
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'register-field__form','placeholder': '이메일'})
        self.fields['username'].widget.attrs.update({'class': 'register-field__form','placeholder': '닉네임'})
        self.fields['password1'].widget.attrs.update({'class': 'register-field__form','placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'class': 'register-field__form','placeholder': '비밀번호 확인'})
        self.fields['name'].widget.attrs.update({'class': 'register-field__form','placeholder': '이름'})
        self.fields['date_of_birth'].widget.attrs.update({'class': 'register-field__form','placeholder': '생년월일 - 1234-56-78'})

    @transaction.atomic  # 모든 함수가 한번에 처리됨.
    def save(self):
        profile = super().save(commit=False)
        # commit=False 바로 저장하지 않고 u_type을 설정하고 저장
        profile.save()

        director = Director.objects.create(profile=profile)
        director.save()

        return profile


class ProfileAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'login-field__form','placeholder': '이메일'})
        self.fields['password'].widget.attrs.update({'class': 'login-field__form','placeholder': '비밀번호를 입력해주세요'})

    def clean(self):
        if self.is_valid():
            # self : form
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invaild login")

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = ActorImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'image-input'})
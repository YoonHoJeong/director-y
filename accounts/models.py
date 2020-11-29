from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

import json

# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        # if not name:
        #     raise ValueError('Users must have an name')
        # if not age:
        #     raise ValueError('Users must have an age')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            # name=name,
            # age=age
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            # name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Profile(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email", max_length=60, unique=True, null=False, blank=False)
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    name = models.CharField(max_length=20, default="", blank=False)
    phone_number = PhoneNumberField(null=False, blank=False, default="")

    # 필수가 아닌 fields
    age = models.PositiveIntegerField(null=True, blank=True)
    name_eng = models.CharField(max_length=20, default="", blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True,  # profile 이미지
                               blank=True,
                               upload_to='image/avatar')
    intro = models.TextField(default="")  # 소개글
    education = models.CharField(max_length=20, null=True, blank=True)
    u_type = models.PositiveSmallIntegerField(null=True)

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # used as the unique identifier
    objects = ProfileManager()

    def __str__(self):
        return self.email

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def user_type(self):
        type = self.u_type

        if type == 1:
            return "director"
        elif type == 2:
            return "actor"
        elif type == 3:
            return "staff"
        else:
            return "unknown"

class Director(models.Model):
    awards = models.TextField()
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.profile.name

class Actor(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, primary_key=True)

    company = models.CharField(max_length=30)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)

    # favorite_character_title = models.CharField(max_length=30)
    # foreign key로 구현?
    favorite_image = models.ImageField(null=True, blank=True)
    specialty = models.CharField(max_length=30)

    def __str__(self):
        return self.profile.name

class Staff(models.Model):
    # profile_... 들은 프로필에 보여질 대표 포토폴리오의 이미지,영상,제목
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, primary_key=True)

    role = models.CharField(max_length=30)

    tool_list = models.CharField(max_length=200)
    def __str__(self):
        return self.profile.name

class SNS(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    url = models.URLField()

class Like(models.Model):
    # from main.models import Movie

    LIKE_CHOICES = ((1, 'movie'),(2, 'director'), (3, 'actor'), (4, 'staff'))
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    type = models.IntegerField(choices=LIKE_CHOICES)

    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
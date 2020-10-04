from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    username = models.CharField(
        max_length=30, unique=True, null=False, blank=False)
    name = models.CharField(max_length=20, default="", blank=False)
    name_eng = models.CharField(max_length=20, default="", blank=True)
    age = models.PositiveIntegerField(null=True, blank=False)
    date_of_birth = models.DateField(null=True, blank=False)
    avatar = models.ImageField(null=True,  # profile 이미지
                               blank=True,
                               upload_to='image/avatar')
    intro = models.TextField(default="")  # 소개글
    # sns = models.URLFied() - 여러개 선택 가능
    # sns_list = models.CharField(max_length=200)
    # def set_sns_list(self, x):
    #     self.sns_list = json.dumps(x)

    # def get_sns_list(self):
    #     return json.loads(self.sns_list)

    # tag_list = models.CharField(max_length=200)

    # def set_tag_list(self, x):
    #     self.tag_list = json.dumps(x)

    # def get_tag_list(self):
    #     return json.loads(self.tag_list)

    education = models.CharField(max_length=20, null=True, blank=True)
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

    """
        introduction
        birth
        education
        awards
        sns link
        profile image
        

    """


class Director(Profile):
    # 추가로 들어갈 field
    # awards - 수상 내역
    awards = models.TextField()


class Actor(Profile):
    """
        company
        height
        weight
        favorite_character_img
        favorite_character_title
        profile_video_title
        profile_video_url
    """
    company = models.CharField(max_length=30)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)

    # favorite_character_title = models.CharField(max_length=30)
    # foreign key로 구현?
    favorite_image = models.ImageField(null=True, blank=True)
    specialty = models.CharField(max_length=30)

# profile_video_title = models.CharField(
#     max_length=20, null=True, blank=False)
# profile_video_url = models.URLField(null=True, blank=False)


class Staff(Profile):
    """
        role
        profile_img_title
        profile_img
    """

    # profile_... 들은 프로필에 보여질 대표 포토폴리오의 이미지,영상,제목

    role = models.CharField(max_length=30)

    tool_list = models.CharField(max_length=200)

    # def set_tag_list(self, x):
    #     self.tool_list = json.dumps(x)

    # def get_tag_list(self):
    #     return json.loads(self.tool_list)

    # profile_img = models.ImageField(null=True, blank=True)
    # profile_img_title = models.CharField(max_length=20, null=True)

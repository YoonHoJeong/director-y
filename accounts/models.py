from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# default user모델로 설정해야함.
# 기본 유저가 갖고 있을 데이터
#


class Profile(AbstractBaseUser):
    age = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(max_length=10,
                            blank=False,)
    date_of_birth = models.DateField()

    nickname = models.CharField(max_length=10,
                                blank=False,
                                unique=True, )

    avatar = models.ImageField(null=True,  # profile 이미지
                               blank=True,
                               upload_to='image/avatar')
    email = models.EmailField(verbose_name='email',
                              max_length=255,
                              unique=True,
                              blank=False,)
    intro = models.TextField()  # 소개글
    # sns = models.URLFied() - 여러개 선택 가능
    # educatioon = models.CharField()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = ['name', 'date_of_birth', 'nickname', 'email']
    # used as the unique identifier
    # blank

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


# class Actor(Profile):


# class Staff(Profile):

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
            # age=age,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=10, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(null=True,  # profile 이미지
                               blank=True,
                               upload_to='image/avatar')
    intro = models.TextField(null=True)  # 소개글
    # sns = models.URLFied() - 여러개 선택 가능
    # educatioon = models.CharField()

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

    """


class Staff(Profile):
    """

    """

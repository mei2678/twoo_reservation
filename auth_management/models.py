from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=200, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sns_icon_url = models.URLField(blank=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def icon_url(self):
        """
        ユーザーのSNSアイコン画像URLを返す。
        1. SNS認証時にプロフィール画像を取得できた場合: sns_icon_url
        2. SNS認証時にプロフィール画像を取得できない場合: デフォルト画像
        """
        if self.sns_icon_url:
            return self.sns_icon_url
        else:
            return staticfiles_storage.url('config/初期プロフィール画像.png')
# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True, default='default_username')
    password = models.CharField(max_length=100)
    reset_password_token = models.CharField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = 'username'  # Specify the field to be used for authentication
    REQUIRED_FIELDS = ['email']  # Add the required fields for user creation (excluding USERNAME_FIELD)

    objects = UserManager()

    def __str__(self):
        return self.username

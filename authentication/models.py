from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from rewards.models import RewardProgram


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = user.is_superuser = user.is_active = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    reward_program = models.ForeignKey(RewardProgram, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


from authentication.signals import save_historical_data  # noqa

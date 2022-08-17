from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
# from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    ADMIN = 'admin'
    USER = 'user'
    ROLES = [(ADMIN, 'Админ'), (USER, 'Пользователь')]


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = PhoneNumberField
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=12, choices=UserRoles.ROLES, default='user')
    images = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

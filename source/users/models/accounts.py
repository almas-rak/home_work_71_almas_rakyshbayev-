from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pic', verbose_name='Аватар')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

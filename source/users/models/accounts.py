from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from users.manegers import UserManager


class GenderChoice(TextChoices):
    Male = 'Male', 'Мужской'
    Female = 'Female', 'женский'
    Not_specified = 'Not_specified', 'Не указан'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )

    birth_date = models.DateField(
        null=True, blank=True,
        verbose_name='Дата рождения'
    )

    liked_posts = models.ManyToManyField(
        verbose_name='Понравившиеся публикации',
        to='posts.Post',
        related_name='user_likes'
    )

    subscriptions = models.ManyToManyField(
        verbose_name='Подписки',
        to='users.Account',
        related_name='subscribers'
    )

    commented_posts = models.ManyToManyField(
        verbose_name='Прокомментированные публикации',
        to='posts.Post',
        related_name='user_comments'
    )

    tel = models.IntegerField(
        null=True, blank=True,
        verbose_name='Номер телефона'
    )

    gender = models.CharField(
        verbose_name='Пол',
        choices=GenderChoice.choices,
        max_length=20,
        default=GenderChoice.Not_specified)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

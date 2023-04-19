# Generated by Django 4.2 on 2023-04-19 16:53

from django.conf import settings
from django.db import migrations, models
import users.manegers


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('objects', users.manegers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(related_name='user_comments', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
        migrations.AddField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AddField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
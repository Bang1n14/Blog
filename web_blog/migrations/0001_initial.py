# Generated by Django 4.0.6 on 2022-07-25 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тема поста')),
                ('text', models.TextField(verbose_name='Сам пост')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации')),
            ],
        ),
    ]

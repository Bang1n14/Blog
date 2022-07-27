from django.db import models
from datetime import date


class Post(models.Model):
    name = models.CharField('Тема поста', max_length=150)
    text = models.TextField('Сам пост')
    date = models.DateField('Дата публикации', default=date.today)
    image = models.ImageField('Добавь картинку', upload_to='image_for_post/')
    """Зачем эта функция"""
    def __str__(self):
        return self.name


""" Необходима добавить лайки коменты и share """



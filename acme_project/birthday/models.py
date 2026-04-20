"""Модели приложения birthday."""

from django.db import models


class Birthday(models.Model):
    """Запись: имя, фамилия (необязательно), дата рождения."""

    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения')

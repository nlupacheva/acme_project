"""Формы приложения birthday."""

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    """Форма создания и редактирования записи о дне рождения."""

    class Meta:
        """Поля и виджеты модели Birthday."""

        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        """Если имя в BEATLES — письмо админу и ValidationError."""
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = (cleaned_data.get('last_name') or '').strip()
        if not first_name:
            return cleaned_data
        full_name = f'{first_name} {last_name}'.strip()
        if full_name in BEATLES:
            # При DEBUG=True не глотаем ошибки записи в каталог писем.
            send_mail(
                subject='Another Beatles member',
                message=f'{full_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=not settings.DEBUG,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
        return cleaned_data

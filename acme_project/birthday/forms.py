# birthday/forms.py
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = (cleaned_data.get('last_name') or '').strip()
        if not first_name:
            return cleaned_data
        full_name = f'{first_name} {last_name}'.strip()
        if full_name in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=f'{full_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                # При DEBUG=True не глотаем ошибки записи (каталог, права) — иначе письма «тихо» пропадают.
                fail_silently=not settings.DEBUG,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
        return cleaned_data

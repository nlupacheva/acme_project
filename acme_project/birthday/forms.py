# birthday/forms.py
from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday

class BirthdayForm(forms.ModelForm):
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__' 
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})}
            
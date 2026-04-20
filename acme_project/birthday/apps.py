"""Конфигурация приложения birthday."""

from django.apps import AppConfig


class BirthdayConfig(AppConfig):
    """Настройки приложения «Дни рождения»."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birthday'

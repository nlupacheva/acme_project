"""Представления для статических страниц."""

from django.shortcuts import render


def homepage(request):
    """Главная страница сайта."""
    return render(request, 'pages/index.html')

"""Представления CRUD и детального просмотра записей о днях рождения."""

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    """Постраничный список записей."""

    model = Birthday
    context_object_name = 'birthdays'
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    paginate_by = 10


class BirthdayMixin:
    """Общие поля для create/update/delete."""

    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayCreateView(BirthdayMixin, CreateView):
    """Создание новой записи."""

    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    """Редактирование существующей записи."""

    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'


class BirthdayDeleteView(BirthdayMixin, DeleteView):
    """Удаление записи (подтверждение по умолчанию)."""
    # Указываем модель, с которой работает CBV...


class BirthdayDetailView(DetailView):
    """Карточка записи с расчётом дней до следующего ДР."""

    model = Birthday

    def get_context_data(self, **kwargs):
        """Добавляет в контекст число дней до дня рождения."""
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context

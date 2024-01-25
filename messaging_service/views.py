from random import sample

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from messaging_service.models import Messages, Clients, MailingSettings


class MessagesCreateView(CreateView):
    """Контроллер для создания сообщений"""
    model = Messages
    fields = ('title', 'body')
    success_url = reverse_lazy('messaging_service:messages-list')


class MessagesListView(ListView):
    """Контроллер для просмотра списка сообщений"""
    model = Messages


class MessagesDetailView(DetailView):
    """Контроллер для просмотра отдельного сообщений"""
    model = Messages


class MessagesUpdateView(UpdateView):
    """Контроллер для редактирования сообщений"""
    model = Messages
    fields = ('title', 'body')
    success_url = reverse_lazy('messaging_service:messages-list')


class MessagesDeleteView(DeleteView):
    """Контроллер для удаления сообщений"""
    model = Messages
    success_url = reverse_lazy('messaging_service:messages-list')


class ClientsCreateView(CreateView):
    """Контроллер для создания нового клиента"""
    model = Clients
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('messaging_service:clients-list')


class ClientsListView(ListView):
    """Контроллер для просмотра списка клиентов"""
    model = Clients


class ClientsDetailView(DetailView):
    """Контроллер для просмотра конкретного клиента"""
    model = Clients


class ClientsUpdateView(PermissionRequiredMixin, UpdateView):
    """Контроллер для редактирования клиентов"""
    model = Clients
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('messaging_service:clients-list')
    permission_required = 'messaging_service.change_clients'


class ClientsDeleteView(DeleteView):
    """Контроллер для удаления клиентов"""
    model = Clients
    success_url = reverse_lazy('messaging_service:clients-list')


class MailingSettingsCreateView(CreateView):
    """Контроллер для создания рассылки"""
    model = MailingSettings
    fields = ('start_date', 'end_date', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('messaging_service:settings-list')


class MailingSettingsUpdateView(PermissionRequiredMixin, UpdateView):
    """Контроллер для редактирования рассылки"""
    model = MailingSettings
    fields = ('start_date', 'end_date', 'period', 'status', 'message', 'client')
    success_url = reverse_lazy('messaging_service:settings-list')
    permission_required = 'messaging_service.change_mailingsettings'


class MailingSettingsDeleteView(DeleteView):
    """Контроллер для удаления рассылки"""
    model = MailingSettings
    success_url = reverse_lazy('messaging_service:settings-list')


class MailingSettingsListView(ListView):
    """Контроллер для просмотра списка рассылок"""
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    """Контроллер для просмотра конкретной рассылки"""
    model = MailingSettings


def homepage(request):
    """Контроллер главной страницы"""
    total_mailings = MailingSettings.objects.count()
    active_mailings = MailingSettings.objects.filter(status=MailingSettings.STATUS_RUN).count()
    unique_clients = Clients.objects.values('email').distinct().count()
    random_articles = sample(list(Blog.objects.all()), 3)

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
        'random_articles': random_articles
    }

    return render(request, 'messaging_service/homepage.html', context)

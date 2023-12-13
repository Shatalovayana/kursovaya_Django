from django.contrib import admin

from messaging_service.models import Clients, Messages, Settings


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'comment',)
    search_fields = ('name',)


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'period', 'status')
    list_filter = ('status', 'period',)

from django.contrib import admin

from messaging_service.models import Clients, Messages, MailingSettings, MessageLog


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'comment', )
    search_fields = ('name', )


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    list_filter = ('title',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'period', 'status', 'message',)
    list_filter = ('status', 'period',)


@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status_try', 'client', 'mailing_settings',)

from django.core.mail import send_mail
from django.utils import timezone
from django.utils.timezone import localtime

from config.settings import EMAIL_HOST_USER
from messaging_service.models import MailingSettings, MessageLog


def send_email(message_settings):
    """Функция для отправки сообщений по почте"""
    today = localtime(timezone.now())
    for client in message_settings.client.all():
        send_it = False
        message_log = MessageLog.objects.filter(client=client, mailing_settings=message_settings).order_by('-last_try').first()
        if message_log is not None:
            date_diff = today - message_log.last_try

        if message_log is None:
            send_it = True
        elif message_settings.period == MailingSettings.ONCE_A_DAY and date_diff.days == 1:
            send_it = True
        elif message_settings.period == MailingSettings.ONCE_A_WEEK and date_diff.days == 7:
            send_it = True
        elif message_settings.period == MailingSettings.ONCE_A_MONTH and date_diff.days == 30:
            send_it = True

        if send_it:
            result = send_mail(
                subject=message_settings.message.title,
                message=message_settings.message.body,
                from_email=EMAIL_HOST_USER,
                recipient_list=[client.email],
                fail_silently=False
            )
            if result > 0:
                MessageLog.objects.create(
                    status_try=MessageLog.STATUS_OK,
                    mailing_settings=message_settings,
                    client_id=client.id
                )
            else:
                MessageLog.objects.create(
                    status_try=MessageLog.STATUS_FAIL,
                    mailing_settings=message_settings,
                    client_id=client.id
                )


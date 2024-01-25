from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Clients(models.Model):
    """Модель Клиента"""
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=300, unique=True, verbose_name='email')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')
    user = models.ManyToManyField(User, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.name} : {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Messages(models.Model):
    """Модель Сообщений"""
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    user = models.ManyToManyField(User, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        permissions = [
            (
                'see_clients',
                'Can see clients'
            ),
            (
                'block_clients',
                'Can block clients'
            ),
        ]


class MailingSettings(models.Model):
    """Модель настройки рассылок"""
    ONCE_A_DAY = 'daily'
    ONCE_A_WEEK = 'weekly'
    ONCE_A_MONTH = 'monthly'
    PERIOD_CHOICES = ((ONCE_A_DAY, 'раз в день'),
                      (ONCE_A_WEEK, 'раз в неделю'),
                      (ONCE_A_MONTH, 'раз в месяц'))
    STATUS_CREATED = 'created'
    STATUS_CLOSED = 'closed'
    STATUS_RUN = 'run'
    STATUS_CHOICES = ((STATUS_CREATED, 'создана'),
                      (STATUS_CLOSED, 'завершена'),
                      (STATUS_RUN, 'запущена'))

    start_date = models.DateTimeField(verbose_name='дата начала рассылки')
    end_date = models.DateTimeField(verbose_name='дата окончания рассылки')
    period = models.CharField(max_length=150, verbose_name='периодичность рассылки', choices=PERIOD_CHOICES)
    status = models.CharField(max_length=150, verbose_name='статус рассылки', choices=STATUS_CHOICES)
    message = models.ForeignKey(Messages, on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ManyToManyField(Clients, verbose_name='клиент')
    user = models.ManyToManyField(User, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'
        permissions = [
            (
                'see_mailing',
                'Can see mailing'
            ),
            (
                'stop_mailing',
                'Can stop mailing'
            ),
        ]


class MailingClient(models.Model):
    """Модель, в которой связаны клиенты и рассылки"""
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)


class MessageLog(models.Model):
    """Модель логов"""
    STATUS_OK = 'OK'
    STATUS_FAIL = 'FAIL'
    STATUS_CHOICES = ((STATUS_OK, 'успешно'),
                      (STATUS_FAIL, 'ошибка')
                      )
    last_try = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки', **NULLABLE)
    status_try = models.CharField(verbose_name='статус рассылки', choices=STATUS_CHOICES, **NULLABLE)
    server_response = models.CharField(max_length=150, default='Нет ответа', verbose_name='ответ сервера')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE)
    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)
    user = models.ManyToManyField(User, verbose_name='Пользователь')
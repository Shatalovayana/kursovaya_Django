from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Clients(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(max_length=300, unique=True, verbose_name='email')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    def __str__(self):
        return f'{self.name} : {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Messages(models.Model):
    title = models.CharField(max_length=300, verbose_name='тема письма')
    body = models.TextField(verbose_name='содержание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Settings(models.Model):
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
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='клиент')

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class MessageLog(models.Model):
    pass

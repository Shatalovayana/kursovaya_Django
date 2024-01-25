from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    """Модель Блога"""
    title = models.CharField(max_length=200, verbose_name='Заголовок', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    user = models.ManyToManyField(User, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

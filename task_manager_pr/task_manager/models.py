from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Малый'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    STATUS_CHOICES = [
        ('not_done', 'Не выполнено'),
        ('done', 'Выполнено'),
    ]

    title = models.CharField(max_length=255, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания задачи')
    deadline_date = models.CharField(max_length=10,verbose_name='Дата-дедлайн задачи')
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium', verbose_name='Уровень приоритета')
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='not_done', verbose_name='Статус')

    def __str__(self):
        return self.title

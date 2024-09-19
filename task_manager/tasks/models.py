from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('NOT_STARTED', 'Не начато'),
        ('IN_PROGRESS', 'В процессе'),
        ('COMPLETED', 'Завершено'),
    ]
    PRIORITY_CHOICES = [
        ('LOW', 'Низкий'),
        ('MEDIUM', 'Средний'),
        ('HIGH', 'Высокий'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_STARTED')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    category = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
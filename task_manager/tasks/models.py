from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Не начато'),
        ('In Progress', 'В процессе'),
        ('Completed', 'Завершено'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    category = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

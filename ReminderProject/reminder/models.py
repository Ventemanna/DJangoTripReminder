from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.gis.db.models import PointField

class CustomUser(AbstractUser):
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True)
    is_first_login = models.BooleanField(default=False)
    telegram_id = models.IntegerField(default=None, null=True)
    chat_id = models.IntegerField(default=None, null=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'custom_users'

class Reminder(models.Model):
    notifications_examples = [
        ('email', 'По email'),
        ('telegram', 'В telegram чат'),
        ('both', 'Email и telegram')
    ]
    transport_types = [
        ('driving', 'автомобиль'),
        ('truck', 'грузовой автомобиль'),
        ('walking', 'пешеход'),
        ('transit', 'общественный транспорт'),
        ('bicycle', 'велосипед'),
        ('scooter', 'электросамокат')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_point = PointField()
    end_point = PointField()
    estimated_departure_time = models.DateTimeField(null=True, blank=True) #translate: предположительное время отправки
    arrival_time = models.DateTimeField(null=True, blank=True)
    transport = models.CharField(choices=transport_types, max_length=10)
    reminder_time = models.DateTimeField(null=True, blank=True)
    notification_method = models.CharField(choices=notifications_examples, default='email', max_length=10)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'reminders'
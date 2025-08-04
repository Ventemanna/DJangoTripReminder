from django.contrib import admin
from .models import CustomUser, Reminder

admin.site.register(CustomUser)
admin.site.register(Reminder)

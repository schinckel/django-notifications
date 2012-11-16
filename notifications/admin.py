# -*- coding: utf-8 -*-

from django.contrib import admin
from notifications.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('recipient',)

admin.site.register(Notification, NotificationAdmin)

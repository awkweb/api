from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ...models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "account_id", "name", "user", "date_created")
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ...models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "available",
        "current",
        "limit",
        "iso_currency_code",
        "unofficial_currency_code",
        "account",
        "date_created",
    )
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

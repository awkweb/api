from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ..models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "name", "transaction_id", "user", "date_created")
    ordering = ["-date"]

    def created(self, obj):
        return naturaltime(obj.date)

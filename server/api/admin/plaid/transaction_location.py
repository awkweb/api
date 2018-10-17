from django.contrib import admin

from ...models import TransactionLocation


@admin.register(TransactionLocation)
class TransactionLocationAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "city", "state")

from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'created_at',
        'id',
        'amount',
        'category',
        'category_id',
        'date',
        'name',
        'payment_meta',
        'pending',
        'pending_transaction_id',
        'pending_transaction_id',
        'transaction_id',
        'transaction_type',
        'transaction_location',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

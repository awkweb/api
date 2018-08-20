from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import TransactionLocation


@admin.register(TransactionLocation)
class TransactionLocationAdmin(admin.ModelAdmin):
    list_display = (
        'transaction',
        'created_at',
        'id',
        'address',
        'city',
        'lon',
        'lat',
        'point',
        'state',
        'store_number',
        'zip_code',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

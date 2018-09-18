from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime
from server.api.models import Balance


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'created_at',
        'id',
        'available',
        'current',
        'limit',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

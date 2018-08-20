from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'balance',
        'institution',
        'created_at',
        'id',
        'a_subtype',
        'a_type',
        'account_id',
        'account_id',
        'mask',
        'name',
        'official_name',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

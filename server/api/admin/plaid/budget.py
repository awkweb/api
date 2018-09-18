from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'amout',
        'user',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

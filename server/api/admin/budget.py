from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ..models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "name", "date_created")
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

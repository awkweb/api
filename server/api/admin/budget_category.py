from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ..models import BudgetCategory


@admin.register(BudgetCategory)
class BudgetCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "date_created")
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

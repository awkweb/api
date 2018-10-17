from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ...models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("item_id", "id", "user", "institution", "date_created")
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

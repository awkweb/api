from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from ...models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("id", "institution_id", "name", "date_created")
    ordering = ["-date_created"]

    def created(self, obj):
        return naturaltime(obj.date_created)

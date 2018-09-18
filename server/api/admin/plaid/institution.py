from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import naturaltime

from server.api.models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'created_at',
        'id',
        'institution_id',
        'name',
    )
    ordering = ['-created_at']

    def created(self, obj):
        return naturaltime(obj.created_at)

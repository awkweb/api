from django.contrib import admin

from ..models import TransactionPaymentMeta


@admin.register(TransactionPaymentMeta)
class TransactionPaymentMetaAdmin(admin.ModelAdmin):
    list_display = ("id", "reference_number", "ppd_id", "payee_name")

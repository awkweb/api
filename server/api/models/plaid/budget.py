from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class Budget(models.Model):
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='accounts',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'api_budget'
        verbose_name = 'budget'
        verbose_name_plural = 'budgets'

    def __str__(self):
        return f'{self.id}'

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return False

    @staticmethod
    def has_create_permission(request):
        return True

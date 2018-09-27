import uuid
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .budget_category import BudgetCategory


class Budget(models.Model):
    """
    A User has many Budgets but an Budget has only one User.
    A BudgetCategory has many Budgets but a Budget has only one BudgetCategory.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(_("amount"), max_digits=10, decimal_places=2)
    name = models.CharField(_("name"), max_length=25)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user")
    )
    budget_category = models.ForeignKey(
        BudgetCategory,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="budgets",
        verbose_name=_("budget category"),
    )
    date_created = models.DateTimeField(_("date_created"), default=timezone.now)

    class Meta:

        verbose_name_plural = "budgets"

    def __str__(self):
        return self.name.title()

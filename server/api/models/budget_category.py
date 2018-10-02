import uuid
from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BudgetCategory(models.Model):
    """
    A User has many BudgetCategories but an BudgetCategory has only one User.
    A BudgetCategory has many Budgets but a Budget has only one BudgetCategory.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=25)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(_("date created"), default=timezone.now)

    class Meta:
        ordering = ["name"]
        db_table = "api_budget_category"
        verbose_name = "budget category"
        verbose_name_plural = "budget categories"

    def __str__(self):
        return self.name.title()

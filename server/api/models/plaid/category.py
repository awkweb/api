import uuid
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """
    A Transaction has many Categories and a Category has many Transactions.
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.CharField(_("category_id"), max_length=50)
    group = models.CharField(_("group"), max_length=50)
    hierarchy = (
        _("hierarchy"),
        ArrayField(models.CharField(max_length=25, blank=True), size=8),
    )

    class Meta:
        db_table = "api_plaid_category"
        verbose_name_plural = "categories"

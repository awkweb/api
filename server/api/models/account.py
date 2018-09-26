from django.conf import settings
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .institution import Institution


class Account(models.Model):
    """
    A User has many Accounts but an Account has only one User.
    An Institution has many Accounts but an Account has only one Institution.
    An Account has many Transactions but a Transaction can have only one Account.
    """

    account_id = models.CharField(_("account_id"), max_length=50)
    mask = models.CharField(_("mask"), max_length=4)
    name = models.CharField(_("name"), max_length=100)
    official_name = models.CharField(_("official_name"), max_length=100)
    subtype = models.CharField(_("subtype"), max_length=50)
    type = models.CharField(_("type"), max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name="accounts"
    )
    date_created = models.DateTimeField(_("date_created"), default=timezone.now)

    class Meta:
        verbose_name_plural = "accounts"

    def __str__(self):
        return self.name.title()

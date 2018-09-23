from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from .institution import Institution


class PlaidToken(models.Model):
    """
    A User has many PlaidTokens but a PlaidToken has only one User.
    Institutions have many PlaidTokens but an PlaidTokens has only one Institution.
    """

    value = models.CharField(_("value"), max_length=100)
    user = models.ForeignKey(
        _("user"), settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    institution = models.ForeignKey(
        _("institution"), Institution, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "plaid tokens"
